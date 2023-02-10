<?php

namespace App\Http\Controllers;

use App\Models\JwtHandler;
use App\Models\Users;
use Illuminate\Http\Request;


class authController extends Controller
{
    // login page
    // calls login method
    public function loginChoose()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {

            $userCheck = new Users();
            $checks = $userCheck->loginCheck($_POST['username'], $_POST['password']);
            if (strlen($checks) == 0) {
                return view('general.index', ['message' => "Login Successfull! Welcome {$_POST['username']}"]);
            } else {
                return view('general.login', ['errorMsg' => $checks]);
            }
        } else {
            return view('general.login');
        }
    }

    // register page
    // handles register method
    public function registerChoose()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {

            $userCheck = new Users();
            $checks = $userCheck->registerCheck(
                $_POST['email'],
                $_POST['username'],
                $_POST['password'],
                $_POST['confirmPassword']
            );
            if (strlen($checks) > 0) {
                return view('general.register', ['errorMsg' => $checks]);
            } else {
                return view('general.login', ['message' => "The user {$_POST['username']} was created, please login."]);
            }
        } else {
            return view('general.register');
        }
    }

    // password change
    // matches the old password with the hash
    // then checks for validity on the new ones, all in passChangeCheck
    public function userChange()
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return view('general.index', ['errorMsg' =>
            "Por favor, realize o login para acessar a dashboard!"]);
        } elseif ($jwtManager->validateToken($token) != 0) {
            return view('general.index', ['errorMsg' =>
            "Por favor, realize o login para acessar a dashboard!"]);
        }


        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $userCheck = new Users();
            $checks = $userCheck->passChangeCheck(
                $_POST['oldpass'],
                $_POST['newpassword'],
                $_POST['confirmpass']
            );
            if (strlen($checks) > 0) {
                return view('users.change', ['errMsg' => $checks]);
            } else {
                return view('users.change', ['message' => "Your password has been changed!"]);
            }
        } else {
            return view('users.change');
        }
    }

    // logout
    // flushes session
    public function logout(Request $request)
    {
        $request->session()->flush();
        return view("general.index", ['message' => 'Logged out!']);
    }
}
