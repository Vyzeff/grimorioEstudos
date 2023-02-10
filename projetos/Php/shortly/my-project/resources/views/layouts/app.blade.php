<!DOCTYPE html>

<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>@yield('title')</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    <link rel="icon" type="image/x-icon" href="{{asset('css/favicone.ico')}}">
    <link media="all" rel="stylesheet" href="{{asset('css/app.css')}}">
</head>

<body>
    <header class="stayup" id="myheader">
        <div>
            <nav class="header">
                <table class="table">
                    <tr scope="row" id="nav" class="navbar">
                        <th scope="col" class="navelement">
                            <a class="link draw" href="\">Home</a>
                        </th>
                        <th scope="col" class="navelement">
                            <a class="link draw" href="\features">Features</a>
                        </th>
                        <th scope="col" class="navelement">
                            <a class="link draw" href="\help">Help</a>
                        </th>

                        @if (session('JWT') === null)
                        <th scope="col" class="navelement">
                            <a class="link draw" href="\login">Login</a>
                        </th>

                        <th class="navelement">
                            <button class="btn btn-dark" type="button">
                                <a href="/register" class="btntext">Get Started</a>
                            </button>
                        </th>
                        @endif

                        @if (session('JWT') !== null)
                        <th scope="col" class="navelement">
                            <a class="link draw" href="\dashboard">Dashboard</a>
                        </th>
                        <th scope="col" class="navelement">
                            <a class="link draw" href="\logout">Logout</a>
                        </th>
                        @endif

                        @if (session('admin') !== null)
                        <th scope="col" class="navelement">
                            <a class="link draw" href="\staff">Staff</a>
                        </th>
                        @endif
                        <th class="navelement">&ensp;</th>
                        <th class="navelement">&ensp;</th>
                        <th class="navelement">&ensp;</th>
                        <th class="navelement">&ensp;</th>
                        <th class="navelement">
                            <a href="/" id="logo">Shortly<span id="logodetail">.io &#8482;</span></a>
                        </th>
                    </tr>
                </table>
            </nav>
        </div>
    </header>
    @if (isset($message))
    <div class="alertbox">
        <div class="alert alert-dark" role="alert">
            <span class="alertmessage"><strong>{{$message}}</strong><button type="button" class="btn-close center" data-bs-dismiss="alert" aria-label="Close"></button></span>
        </div>
    </div>

@endif
@if (isset($errorMsg))
    <div class="alertbox">
        <div class="alert alert-danger " role="alert">
            <h5>Desculpe, algo deu errado:</h5>
            {{$errorMsg}}<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    </div>
@endif
    <main class="content">
        @yield('content')
    </main>
    <footer class="flex-container">
        <div class="foothelp">
            <span class="footlist"><strong>Products</strong>
            <ul>
                <li><a href="/features">Analytics</a></li>
            </ul>
            </span>
            <span class="footlist"><strong>Community</strong>
            <ul>
                <li><a href="/features">Our Forums</a></li>
            </ul>
            </span>
            <span class="footlist"><strong>About Us</strong>
            <ul>
                <li><a href="/features">Our History</a></li>
            </ul>
            </span>
            <span class="footlist"><strong>Information</strong>
            <ul>
                <li><a href="/help">Documentation</a></li>
            </ul>
            </span>
        </div>
        <small id="helper"><a href="/help">shortly@business.io</a></small>
    </footer>
</body>
@yield('scripts')
<script src="https://019c-2804-431-c7e3-189-c800-a74a-1a9c-927e.sa.ngrok.io/js/app.js"></script>
</html>


