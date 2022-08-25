@extends('layouts.app')

@section('title') staff @endsection

@section('content')

<p>manage user</p>


@if (isset($user))
    @foreach ($user as $item)
        <p>username {{$item['username']}}</p>
        <p>email {{$item['email']}}</p>
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

