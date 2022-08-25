<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;

class Users extends Model
{
    use HasFactory;

    protected $fillable = [
        'username',
        'email',
        'hashPassword',
        'accTypeId',
    ];

    protected function createUser($email, $username, $hashPass, $accType = 1)
    {
        Users::create([
            'username' => $username,
            'email' => $email,
            'hashPassword' => $hashPass,
            'accTypeId' => $accType,
        ]);
        return 0;
    }

    protected function loginSession($id, $username, $accType)
    {
        //session(['id' => $id]);
        //session(['username' => $username]);
        //session(['accType' => $accType]);
        $jwtManager = new JwtHandler();
        try {
            $token = $jwtManager->newJwtToken($username, $id, $accType);

            session(['JWT' => $token->toString()]);
        } catch (\Throwable $err) {
            return $err;
        }
        if ($accType == 0) {
            session(['admin' => true]);
        }
        return 0;
    }

    protected function inputCheck($username, $password, $email = 0, $confirmPass = 0)
    {
        $err = "";

        //username check
        if (strlen($username) >= 21) {
            $err .= "Your username must contain no more than 20 digits";
        } elseif (preg_match('/[\'^£$%&*()}{@#~?><>,|=_+¬-]/', $username)) {
            $err .= "You cannot use special characters in your username!";
        }

        //login or register check
        if ($email != 0) {
            //email check
            if (preg_match('/[\'^£$%&*()}{#~?><>,|=_+¬-]/', $email)) {
                $err .= "Please input a valid email!!" . " < >";
            }
            //email and username db check
            if (
                Users::where('username', $username)->count() != 0 ||
                Users::where('email', $email)->count() != 0
            ) {
                $err .= "Username or Email taken.";
            }

            // password check
            if (!empty($password) && strcmp($password, $confirmPass) == 0) {

                if (strlen($password) <= '8') {
                    $err .= "Your password must contain at least 8 digits!";
                } elseif (strlen($password) >= '21') {
                    $err .= "Your password must contain no more than 20 digits";
                } elseif (!preg_match("#[0-9]+#", $password)) {
                    $err .= "Your password must contain at least 1 number!";
                } elseif (!preg_match("#[A-Z]+#", $password)) {
                    $err .= "Your password must contain at least 1 capital letter!";
                } elseif (!preg_match("#[a-z]+#", $password)) {
                    $err .= "Your password must contain at least 1 lowercase letter";
                } elseif (preg_match('/[\'^£$%&*()}{@#~?><>,|=_+¬-]/', $password)) {
                    $err .= "You cannot use special characters in your password!";
                }
            } else {
                $err .= "Please input and confirm your password. ";
            }
        } else {
            if (Users::where('username', $username)->count() == 0) {
                $err .= "Incorrect username or password. ";
            }
        }
        return $err;
    }

    public function registerCheck($email, $username, $password, $confirmPass, $accType = 1)
    {
        $checks = $this->inputCheck($username, $password, $email, $confirmPass);
        if (strlen($checks) > 0) {
            return $checks;
        }
        $hash = Hash::make($password);
        if ($this->createUser($email, $username, $hash, $accType) == 0) {
            return $checks;
        } else {
            $checks .= "Error during user creation, please wait a few minutes and try again.";
            return $checks;
        }
    }

    public function loginCheck($username, $password)
    {
        $checks = $this->inputCheck($username, $password);
        if (strlen($checks) > 0) {
            return $checks;
        }

        if ($this->passwordCheck($password, $username) != 0) {
            $checks .= "Incorrect username or password.";
            return $checks;
        }
        $rawQuery = DB::select("SELECT id, hashPassword, accTypeId FROM users WHERE username = '{$username}' LIMIT 1");
        $query = json_decode(json_encode($rawQuery), true);

        if ($this->loginSession($query[0]['id'], $username, $query[0]['accTypeId']) == 0) {
            return $checks;
        } else {
            $checks .= "Error during login, please wait some time and retry.";
            return $checks;
        }
    }

    protected function passwordCheck($password, $username = 0)
    {
        if ($username == 0) {
            $token = session('JWT', 0);
            if ($token == 0) {
                return 1;
            }
            $jwtManager = new JwtHandler();
            $parsedToken = $jwtManager->parseToken($token);
            $thisUser = $parsedToken->claims()->get('username');
            $rawQuery = DB::table('users')->select('hashPassword')->where('username', '=', "$thisUser")->get();
            $query = json_decode(json_encode($rawQuery), true);
            if (Hash::check($password, $query[0]['hashPassword']) == true) {
                return 0;
            } else {
                return 1;
            }
        } else {
            $rawQuery = DB::table('users')->select('hashPassword')->where('username', '=', $username)->get();
            $query = json_decode(json_encode($rawQuery), true);
            if (Hash::check($password, $query[0]['hashPassword']) == true) {
                return 0;
            } else {
                return 1;
            }
        }
    }

    public function passChangeCheck($oldPass, $newPass, $confirmNew, $username = 0)
    {
        $err = "";
        // password check
        if (!empty($oldPass)) {
            if ($username != 0) {
                if ($this->passwordUpdate($newPass, $username) != 0) {
                    $err .= "Error during update, please try again later.";
                }
                return $err;
            }
            if ($this->passwordCheck($oldPass) == 0) {
                if (
                    !empty($newPass) && !empty($confirmPass)
                    && strcmp($newPass, $confirmNew) == 0
                ) {
                    if (strlen($newPass) <= '8') {
                        $err .= "Your password must contain at least 8 digits!";
                    } elseif (strlen($newPass) >= '21') {
                        $err .= "Your password must contain no more than 20 digits";
                    } elseif (!preg_match("#[0-9]+#", $newPass)) {
                        $err .= "Your password must contain at least 1 number!";
                    } elseif (!preg_match("#[A-Z]+#", $newPass)) {
                        $err .= "Your password must contain at least 1 capital letter!";
                    } elseif (!preg_match("#[a-z]+#", $newPass)) {
                        $err .= "Your password must contain at least 1 lowercase letter";
                    } elseif (preg_match('/[\'^£$%&*()}{@#~?><>,|=_+¬-]/', $newPass)) {
                        $err .= "You cannot use special characters in your password!";
                    }
                }
            } else {
                $err .= "Please input and confirm your password.";
            }
        } else {
            $err .= "Please input and confirm your password. ";
        }
        if (strlen($err) == 0) {
            if ($this->passwordUpdate($newPass, $username) != 0) {
                $err .= "Error during update, please try again later.";
            }
        }
        return $err;
    }

    protected function passwordUpdate($newPass, $username = 0)
    {
        if ($username == 0) {
            $jwtManager = new JwtHandler();
            $token = session('JWT');
            $parsedToken = $jwtManager->parseToken($token);
            $username = $parsedToken->claims()->get('username');
        }
        $newHash = Hash::make($newPass);
        try {
            DB::table('users')->where('username', '=', "$username")->update(['hashPassword' => "$newHash"]);
            return 0;
        } catch (\Throwable $th) {
            return $th;
        }
    }

    public function getUser($id)
    {

        $rawQuery = DB::select("SELECT * FROM users WHERE id = '{$id}'");
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }

    public function getAllUsers()
    {
        $rawQuery = Users::all();
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }

    public function deleteUser($id)
    {
        $linkManager = new Links();
        $userLinks = $linkManager->getAllLinks($id);

        foreach ($userLinks as $key => $value) {
            $linkManager->deleteLink($value['id']);
        }
        Users::destroy($id);
        return 0;
    }
}
