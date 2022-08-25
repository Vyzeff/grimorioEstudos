@extends('layouts.app')

@section('title') staff @endsection

@section('content')

<h3>All Links:</h3>
<a href="/staff">Staff</a>
<a href="/staff/users">users</a>


@if (isset($userLinks))
<table class="table">
    <tr scope="row">
        <th scope="col">Link Id</th>
        <th scope="col">Short Link</th>
        <th scope="col">Original Link</th>
        <th scope="col">Manage Link</th>
    </tr>
    @foreach ($userLinks as $item)
        <tr scope="row">
            <td>{{$item['id']}}</td>
            <td><a href="/i/{{$item['shortLink']}}">shortly.io/i/{{$item['shortLink']}}</a></td>
            <td><a href="{{$item['originLink']}}">{{$item['originLink']}}</a></td>
            <td><a href="/dashboard/link/{{$item['id']}}">Manage</a></p></td>
        </tr>
    @endforeach
</table>
@endif
@endsection

