@extends('layouts.app')

@section('title') change password @endsection

@section('content')

<p>change password</p>


 <form method="POST" action="/staff/change">
            @csrf

            <!-- USERNAME Address -->
            <div>
                <input id="username" class="" type="text" name="username" required autofocus placeholder="Username"/>
            </div>
            <!-- USERNAME Address -->
            <div>
                <input id="oldpass" class="" type="password" name="oldpass" required  placeholder="Old Password"/>
            </div>

            <!-- Password -->
            <div class="mt-4">
                <input id="newpassword" class="block mt-1 w-full"
                                type="password"
                                name="newpassword"
                                required placeholder="New Password" />
            </div>
            <!-- Confirm Password -->
            <div class="mt-4">
                <input id="confirmpass" class="block mt-1 w-full"
                                type="password"
                                name="confirmpass"
                                required placeholder="Confirm New Password" />
            </div>

                <button class="ml-3">
                    {{ __('Confirm') }}
                </button>
            </div>
        </form>

@endsection
