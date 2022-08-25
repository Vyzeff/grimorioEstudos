<?php

namespace App\Http\Controllers;

use App\Models\Links;

class homeController extends Controller
{


    public function index()
    {
        //$token = $testJwT->newJwtToken("vyzeff", 1);

        //echo $token->headers()->get('shortly') . "<br>"; // will print "bar"
        //echo $token->claims()->get('id') . "<br>"; // will print "1"

        //$tokenString = $token->toString();
        //$token = session('JWT', 'DEU MERDA RAPAZIADA');
        //echo $token;
        //$testJwT = new JwtHandler();
        //echo $testJwT->validateToken($token) . "<br>";
        //$tokenTest = $testJwT->parseToken($token);
        //echo $tokenTest->headers()->get('shortly') . "<br>";
        //echo $tokenTest->claims()->get('id');
        //echo $tokenTest->claims()->get('username');

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
        $result = $linkCreator->checkLink($_POST['link'], 1);
        if ($result != 1) {
            return view('general.index', ["message" => "Your link shortly.io/{$result} was created."]);
        } else {
            return view('general.error', ['errorMsg' => "Failed Link Creation!"]);
        }
    }
}
