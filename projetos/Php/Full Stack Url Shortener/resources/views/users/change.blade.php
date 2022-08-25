@extends('layouts.app')

@section('title') change password @endsection

@section('content')

<div><h3>Change your password here!</h3></div>

<span>please provide your old password, together with your new one and repeat it one more time for confirmation.</span>



 <form method="POST" action="/dashboard/change">
            @csrf

            <!-- USERNAME Address -->
            <div>
                <input id="oldpass" class="" type="password" name="oldpass" required autofocus placeholder="Old Password"/>
            </div>

            <!-- Password -->
            <div class="">
                <input id="newpassword" class=""
                                type="password"
                                name="newpassword"
                                required placeholder="New Password" />
            </div>
            <!-- Confirm Password -->
            <div class="">
                <input id="confirmpass" class="block mt-1 w-full"
                                type="password"
                                name="confirmpass"
                                required placeholder="Confirm New Password" />
            </div>

                <button class="btn btn-dark" type="button">
                    Confirm
                </button>
            </div>
        </form>

@endsection
