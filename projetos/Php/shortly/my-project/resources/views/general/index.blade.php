@extends('layouts.app')

@section('title') Shortly @endsection

@section('content')
<section>
    <div class="bigh">
        <div > {{-- big words --}}
            <h2 class="pageheader"><strong>Your Brand</strong></h2>
            <h4>Our Links</h4>
        </div>
        <div><p>Shorten, personalize, and share
            fully branded URLs.</p></div>

            @if (session('JWT') === null)
                <div>
                    <button class="btn btn-dark" type="button" >
                        <a href="\register" class="btntext">Start for free</a>
                    </button>
                </div>
            @endif
    </div>
</section>

<section>
    <div class="linkform">
        <form method="POST" action="/" class="linkinput">
            @csrf
            <!-- LINK Address -->
            <div class="linkinput">
                <input id="link" class="" name="link" required placeholder="Your Link Here" />
                <div class="linkbutton">
                    <button type="submit" class="btn btn-dark " id="submitlink">
                        <span class="btntext">Create your first link!</span>
                    </button>
                </div>
                <div class="linkdesc">
                    <small>By clicking Shorten URL, you agree to Shortly's <a href="/">Terms of Use</a>,  <a href="/">Privacy Policy</a> and <a href="/">Cookie Policy</a></small>
                </div>
            </div>


        </form>
    </div>

    <div> <h3>Get the most out of each link you share</h3> </div>

    <div>
        <h3>See what we can do!</h3>
        <p><mark>Shortly.io</mark> provides advanced features that will let you, from person to enterprise, get all the benefits of link shortening</p>
    </div>
    <div class="dropdowndisplay">
        <div data-dropdown="1" class="dropdown">
            <span><strong>Click Access and Detailed Statistics</strong></span>
            <h6 data-content="1" class="hidden dropdown-content">Track the popularity of each link with our comprehensive tools</h6>
        </div>
        <div data-dropdown="2" class="dropdown">
            <p><strong>API</strong></p>
            <h6 data-content="2" class="hidden dropdown-content">Quickly extract data with our simple to use API</h6>
        </div>
        <div data-dropdown="3" class="dropdown">
            <p><strong>Many Domains</strong></p>
            <h6 data-content="3" class="hidden dropdown-content">Have multiple domains linked to the same account, each with different settings and analytics</h6>
        </div>
    </div>


    <div class="btncenter"><button type="button" class="btn btn-dark"><a class="btntext" href="/features">All of our features</a></button></div>
</section>
<section>
    <h2>Easy to get started</h2>
    <h4>free to use, these are things we know everyone loves.</h4>
    <div class="btncenter"><button type="button" class="btn btn-dark"><a class="btntext" href="/register">Let's go</a></button></div>

</section>

@endsection
