<?php

namespace App\Http\Controllers;

use App\Models\apiHandler;
use Illuminate\Http\Request;

use function PHPUnit\Framework\isJson;

class apiController extends Controller
{
    public function handleToken($token)
    {
        // SOME LOGIC
        $apiHandler = new apiHandler();
        $data = $apiHandler->handleToken($token);

        if (!isJson($data)) {
            return view('api', ['error' => $data]);
        }

        return view('api', ['data' => $data]);
    }
}
