@extends('layouts.app')

@section('title') Error @endsection

@section('content')

<h2>Sorry, something went wrong</h2>

@if (isset($errorMsg))

<h1>The following error occured:</h1>

<p>{{$errorMsg}}</p>

@endif

@endsection


