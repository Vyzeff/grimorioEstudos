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

    <link media="all" rel="stylesheet" href="{{asset('css/app.css')}}">
</head>

<body>
    <header class="header" id="myheader">
        <div>
            <nav>
                <table class="table">
                    <tr scope="row" id="nav" class="navbar">
                        <th scope="col" class="navelement">
                            <a class="link" href="\">Home</a>
                        </th>
                        <th scope="col" class="navelement">
                            <a class="link" href="\features">Features</a>
                        </th>
                        <th scope="col" class="navelement">
                            <a class="link" href="\help">Help</a>
                        </th>

                        @if (session('JWT') === null)
                        <th scope="col" class="navelement">
                            <a class="link" href="\login">Login</a>
                        </th>

                        <th class="navelement">
                            <button class="btn btn-dark" type="button">
                                <a href="/register">Get Started</a>
                            </button>
                        </th>
                        @endif

                        @if (session('JWT') !== null)
                        <th scope="col" class="navelement">
                            <a class="link" href="\dashboard">Dashboard</a>
                        </th>
                        <th scope="col" class="navelement">
                            <a class="link" href="\logout">Logout</a>
                        </th>
                        @endif

                        @if (session('admin') !== null)
                        <th scope="col" class="navelement">
                            <a class="link" href="\staff">Staff</a>
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
        @if (isset($message))

            <div class="alert alert-dark" role="alert">
                <span class="alertmessage"><strong>{{$message}}</strong><button type="button" class="btn-close center" data-bs-dismiss="alert" aria-label="Close"></button></span>
            </div>
        @endif
        @if (isset($errorMsg))
            <div class="alert alert-danger" role="alert">
                <h5>Desculpe, algo deu errado:</h5>
                {{$errorMsg}}<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        @endif
        <hr>
    </header>
    <main class="content flex-container">
        @yield('content')
    </main>
    <footer>
        <h4><a href="/help">shortly@help.io</a></h4>

        <span>Product</span>
        <ul>
            <li>Test 1</li>
        </ul>

        <span>Community</span>
        <ul>
            <li>test2</li>
        </ul>

        <span>About</span>
        <ul>
            <li>test3</li>
        </ul>

        <span>Resources</span>
        <ul>
            <li>test4</li>
        </ul>
    </footer>
</body>
@yield('scripts')
<script src="{{asset('js/app.js')}}"></script>
</html>


