@extends('layouts.app')

@section('title') staff @endsection

@section('content')

<h3>Manage User</h3>

@if (isset($user))
    @foreach ($user as $item)
        <p>Username: {{$item['username']}}</p>
        <p>Email: {{$item['email']}}</p>
        <p>Account Type: {{$item['accTypeId']}}</p>
    @endforeach
@endif

<form method="POST" action="/staff/users/{{$item['id']}}" >
    @csrf
    <button type="button" class="btn btn-dark">
        DELETE USER
    </button>
</form>

@endsection

