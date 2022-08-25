<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class apiController extends Controller
{
    public function verifyToken($token)
    {
        // SOME LOGIC
        return view('api', ['message' => "THIS IS YOUR TOKEN {$token}"]);
    }
}
