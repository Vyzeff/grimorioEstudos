@extends('layouts.app')

@section('title') Register @endsection

@section('content')

<h3>Create and account</h3>
<div class="formdisplay">
    <form method="POST" action="/register">
        @csrf

        <!-- Email Address -->
        <div>
            <input id="email" type="email" class="inputcontrol" name="email" required autofocus placeholder="Email" />
        </div>

        <!-- USERNAME -->
        <div class="forminput">
            <input id="username" class="inputcontrol" name="username" required autofocus placeholder="Username" />
        </div>

        <!-- Password -->
        <div class="forminput">
            <input id="password" class="inputcontrol" type="password" name="password"
                            required autocomplete="current-password"  placeholder="Password"
                            pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
                            title="Must contain at least one number and
                            one uppercase and lowercase letter, and at least 8 or more characters"/>
        </div>

        <!-- Confirm Password -->
        <div class="forminput">
            <input class="inputcontrol" id="confirmPassword"
                            type="password"
                            name="confirmPassword"
                            required autocomplete="current-password"  placeholder="Confirm password"/>
        </div>
                <!-- An element to toggle between password visibility -->
                <div class="showbutton linkbutton">
                    <button id="showpass" type="button" class="btn btn-dark test"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
                        <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
                        <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                        </svg></button>
                </div>
    <div class="linkbutton">
        <button id="registerTest" class="btn btn-dark" type="submit">
            {{ 'Register' }}
        </button>
    </div>

        </div>
    </form>
    <span><small>By creating your account, you agree to Shortly's <a href="/">Terms of Use</a>,  <a href="/">Privacy Policy</a> and <a href="/">Cookie Policy</a></small>
    </span>
</div>
<div>
    <h5>Already have an account? <small><a href="/login">Sign in</a></small></h5>
</div>
@endsection
