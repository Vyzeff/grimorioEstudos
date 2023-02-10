@extends('layouts.app')

@section('title') staff @endsection

@section('content')

<h3>All Users:</h3>
<a href="/staff">Staff</a>
<a href="/staff/links">Links</a> <br>
<a href="/staff/change">Change a users password</a>



@if (isset($users))
<table class="table">
    <tr scope="row">
        <th scope="col">User Id</th>
        <th scope="col">Username</th>
        <th scope="col">User Email</th>
    </tr>
    @foreach ($users as $item)
    <tr scope="row">
        <td>{{$item['id']}}</td>
        <td>{{$item['username']}}</td>
        <td>{{$item['email']}}</td>
        <td><a href="/staff/users/{{$item['id']}}">Manage</a></td>
    </tr>
    @endforeach
</table>
@endif
<form method="get" action="/staff/users/create" >
    @csrf
    <button class="btn btn-dark">
        Create new User
    </button>
</form>

@endsection

