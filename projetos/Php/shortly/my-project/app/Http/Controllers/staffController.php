<?php

namespace App\Http\Controllers;

use App\Models\DataCollector;
use App\Models\JwtHandler;
use App\Models\Links;
use App\Models\Users;

class staffController extends Controller
{
    // deals with the staff dashboard
    // if the users isn't logged in or isn't admin, go home
    public function staffDash()
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return redirect('/');
        } elseif ($jwtManager->validateToken($token) != 0) {
            return redirect('/');
        }

        $parsedToken = $jwtManager->parseToken($token);

        if ($parsedToken->claims()->get('accType') != 0) {
            return redirect('/');
        }
        return view('users.admin.staff');
    }

    // gets all of the user data
    // namely, all usernames and ids
    public function staffUsers()
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return redirect('/');
        } elseif ($jwtManager->validateToken($token) != 0) {
            return redirect('/');
        }

        $parsedToken = $jwtManager->parseToken($token);

        if ($parsedToken->claims()->get('accType') != 0) {
            return redirect('/');
        }
        $userManager = new Users();
        $allUsers = $userManager->getAllUsers();
        return view('users.admin.users', ['users' => $allUsers]);
    }

    // gets all of the link data
    // namely, all links and ids
    public function staffLinks()
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return redirect('/');
        } elseif ($jwtManager->validateToken($token) != 0) {
            return redirect('/');
        }

        $parsedToken = $jwtManager->parseToken($token);

        if ($parsedToken->claims()->get('accType') != 0) {
            return redirect('/');
        }

        $linkManager = new Links();
        $allLinks = $linkManager->getAllLinks();
        return view('users.admin.links', ['userLinks' => $allLinks]);
    }

    // gets 1 link data
    // handles link deletion
    public function manageLink($id)
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return redirect('/');
        } elseif ($jwtManager->validateToken($token) != 0) {
            return redirect('/');
        }

        $parsedToken = $jwtManager->parseToken($token);

        if ($parsedToken->claims()->get('accType') != 0) {
            return redirect('/');
        }

        $linkManager = new Links();
        $dataManager = new DataCollector();

        $browserData = $dataManager->getBrowserData($id);
        $osData = $dataManager->getOsData($id);
        $link = $linkManager->getLink($id);

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            echo $linkManager->deleteLink($id);
            return redirect("/staff/links");
        }
        return view('users.admin.manageLink', ['link' => $link, 'osData' => $osData, 'browserData' => $browserData]);
    }

    // gets 1 user data
    // handles user deletion
    public function manageUsers($id)
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return redirect('/');
        } elseif ($jwtManager->validateToken($token) != 0) {
            return redirect('/');
        }

        $parsedToken = $jwtManager->parseToken($token);

        if ($parsedToken->claims()->get('accType') != 0) {
            return redirect('/');
        }

        $userManager = new Users();
        $user = $userManager->getUser($id);


        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            echo $userManager->deleteUser($id);
            return redirect("/staff/users");
        }
        return view('users.admin.manageUser', ['user' => $user]);
    }

    // handles the account creation
    // can create new admins, just create a account with id type 0
    public function staffCreate()
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return redirect('/');
        } elseif ($jwtManager->validateToken($token) != 0) {
            return redirect('/');
        }

        $parsedToken = $jwtManager->parseToken($token);

        if ($parsedToken->claims()->get('accType') != 0) {
            return redirect('/');
        }

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {

            $userCheck = new Users();
            $checks = $userCheck->registerCheck(
                $_POST['email'],
                $_POST['username'],
                $_POST['password'],
                $_POST['confirmPassword'],
                $_POST['accType']
            );

            if (strlen($checks) == 0) {
                return view('users.admin.users', ['message' => "The user {$_POST['username']} was created."]);
            } else {
                return view('users.admin.create', ['errorMsg' => $checks]);
            }
        }

        return view('users.admin.create');
    }

    // changes any user password
    // still checks for password validity
    public function staffChange()
    {
        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token == 0) {
            return redirect('/');
        } elseif ($jwtManager->validateToken($token) != 0) {
            return redirect('/');
        }


        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $userManager = new Users();
            $checks = $userManager->passChangeCheck(
                $_POST['oldpass'],
                $_POST['newpassword'],
                $_POST['confirmpass'],
                $_POST['username']
            );
            if (strlen($checks) > 0) {
                return view('users.admin.change', ['errorMsg' => $checks]);
            } else {
                return view('users.admin.change', ['message' => 'The password has been changed.']);
            }
        } else {
            return view('users.admin.change');
        }
    }
}
