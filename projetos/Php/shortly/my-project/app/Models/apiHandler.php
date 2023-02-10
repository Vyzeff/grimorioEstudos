<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\JwtHandler;
use App\Models\Users;
use App\Models\Links;

class apiHandler extends Model
{
    use HasFactory;

    protected function getData($id)
    {

        $userHandler = new Users();
        $userData = $userHandler->getUserData($id);
        $userArray = ['userData' => $userData];

        $linkHander = new Links();
        $linkData = $linkHander->getAllLinks($id);
        $linksArray = ['linkData' => $linkData];

        $allData = array_merge($userArray, $linksArray);
        return json_encode($allData);
    }

    public function handleToken($token)
    {
        $err = "";

        // $jwtManager = new JwtHandler();
        // try {
        //     if ($jwtManager->validateToken($token) != 0) {
        //       $err .= "Invalid Token.";
        //    }
        //} catch (\Throwable $th) {
        //    $err .= "Invalid Token, please verify your key.";
        // }


        if (strlen($err) != 0) {
            return $err;
        }
        //$parsedToken = $jwtManager->parseToken($token);
        //$userId = $parsedToken->claims()->get('id');

        //$userData = $this->getUserData($userId);
        $userData = $this->getData($token);

        return $userData;
    }
}
