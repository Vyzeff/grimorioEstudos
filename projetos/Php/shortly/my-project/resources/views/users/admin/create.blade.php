@extends('layouts.app')

@section('title') create @endsection

@section('content')

<h3>Create a new User</h3>
<small>for the creation of another administrator, please input a account type id of 0</small>
 <form method="POST" action="/staff/users/create">
            @csrf

            <!-- Email Address -->
            <div>
                <input id="email" type="email" class="" name="email" required autofocus placeholder="Email" />
            </div>

            <!-- USERNAME -->
            <div>
                <input id="username" class="" name="username" required  placeholder="Username" />
            </div>

             <!-- ACCOUNT ID -->
             <div>
                <input id="accType" class="" name="accType" required  placeholder="Account Type Id" />
            </div>

            <!-- Password -->
            <div class="">
                <input id="password"
                                type="password"
                                name="password"
                                required autocomplete="current-password"  placeholder="Password"
                                pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                                title="Must contain at least one number
                                and one uppercase and lowercase letter, and at least 8 or more characters"/>
            </div>

            <!-- Confirm Password -->
            <div class="">
                <input id="confirmPassword"
                                type="password"
                                name="confirmPassword"
                                required autocomplete="current-password"  placeholder="Confirm password"/>
            </div>

                <button class="ml-3">
                    {{ 'Create' }}
                </button>
            </div>
        </form>

@endsection
