<?php

namespace App\Http\Controllers;

use App\Models\JwtHandler;
use App\Models\Links;

class homeController extends Controller
{


    public function index()
    {
        return view('general.index');
    }

    public function features()
    {
        return view('general.features');
    }

    public function help()
    {
        return view('general.help');
    }

    public function link()
    {
        $linkCreator = new Links();

        $jwtManager = new JwtHandler();
        $token = session('JWT', 0);

        if ($token != 0) {
            $parsedToken = $jwtManager->parseToken($token);
            $result = $linkCreator->checkLink($_POST['link'], $parsedToken->claims()->get('id'));
        } else {
            $result = $linkCreator->checkLink($_POST['link'], 1);
        }

        if ($result != 1) {
            return view('general.index', ["message" => "Your link shortly.io/{$result} was created."]);
        } else {
            return view('general.error', ['errorMsg' => "Failed Link Creation!"]);
        }
    }
}
