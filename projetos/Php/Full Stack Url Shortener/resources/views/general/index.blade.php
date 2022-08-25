@extends('layouts.app')

@section('title') Shortly @endsection

@section('content')
<div> {{-- big words --}}
    <h2>Your Brand</h2>
    <h4>Our Links</h4>
</div>

<div><p>Shorten, personalize, and share
    fully branded short URLs.</p></div>

    @if (session('JWT') === null)
        <div>
            <button class="btn btn-dark" type="button" >
                <a href="\register">Start for free</a>
            </button>
        </div>
    @endif
<section>
    <div class="linkform">
        <form method="POST" action="/">
            @csrf

            <!-- LINK Address -->
            <div class="linkinput">
                <input id="link" class="" name="link" required placeholder="Your Link Here" />
            </div>
            <div class="linkbutton">
                <button type="submit" class="btn btn-dark">
                    Create your first link!
                </button>
            </div>
            <div class="linkdesc">
                <small>By clicking Shorten URL, you agree to Shortly's <a href="/">Terms of Use</a>,  <a href="/">Privacy Policy</a> and <a href="/">Cookie Policy</a></small>
            </div>
        </form>
    </div>

    <div> <h3>Get the most out of each link you share</h3> </div>

    <div>
        <h3>See how it works</h3>
        <p><mark>Shortly.io</mark> provides advanced features that will let you, from person to enterprise, get all the benefits of link shortening</p>
    </div>

    <div>
        <small data-content="1" class="hidden dropdown-content">Track the popularity of each link with our comprehensive tools</small>
        <p data-dropdown="1" class="dropdown">dropdown 1: <strong>Click & Access  Detailed Statistics</strong></p>
    </div>
    <div>
        <small data-content="2" class="hidden dropdown-content">Quickly extract data with our easy to use API</small>
        <p data-dropdown="2" class="dropdown">dropdown 2: <strong>API</strong></p>
    </div>
    <div>
        <small data-content="3" class="hidden dropdown-content">Have multiple domains linked to the same account, each with different settings and analytics</small>
        <p data-dropdown="3" class="dropdown">dropdown 3: <strong>Many Domains</strong></p>
    </div>

    <div><button type="button" class="btn btn-dark"><a class="text-normal" href="/features">All of our features</a></button></div>
</section>
<section>
    <h2>Easy to get started</h2>
    <h4>free to use, these are things we know everyone loves.</h4>
    <div><button type="button" class="btn btn-dark"><a class="text-normal" href="/register">Let's go</a></button></div>

</section>

@endsection
