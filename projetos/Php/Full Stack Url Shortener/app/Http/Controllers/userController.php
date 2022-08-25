<?php

namespace App\Http\Controllers;

use App\Models\DataCollector;
use App\Models\JwtHandler;
use App\Models\Links;

class userController extends Controller
{
    public function dashboard()
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

        $parsedToken = $jwtManager->parseToken($token);
        $linkManager = new Links();
        $userLinks = $linkManager->getAllLinks($parsedToken->claims()->get('id'));

        return view('users.dashboard', ['userLinks' => $userLinks]);
    }

    public function manageLink($id)
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
        $parsedToken = $jwtManager->parseToken($token);

        $linkManager = new Links();
        $dataManager = new DataCollector();

        $browserData = $dataManager->getBrowserData($id);
        $osData = $dataManager->getOsData($id);
        $link = $linkManager->getLink($id);

        if ($link[0]['userId'] != $parsedToken->claims()->get('id')) {
            return redirect("/dashboard/");
        }

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            echo $linkManager->deleteLink($id);
            return redirect("/dashboard/");
        }
        return view('users.link', ['link' => $link, 'osData' => $osData, 'browserData' => $browserData]);
    }

    public function userLink()
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

        $parsedToken = $jwtManager->parseToken($token);

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {

            $linkManager = new Links();
            $newLink = $linkManager->checkLink($_POST['link'], $parsedToken->claims()->get('id'), $_POST['customChunk']);
            if ($newLink != 1) {
                return view('users.create', ['message' => "Your link shortly.io/{$_POST['customChunk']} was created!"]);
            } else {
                return view('users.create', ['errorMsg' => "Failed link Creation"]);
            }
        } else {
            return view('users.create');
        }
    }
}
