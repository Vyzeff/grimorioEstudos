@extends('layouts.app')
<style>html { background: #D3D0CB}</style>
@section('title') dashboard @endsection

@section('content')
<h3>This is your dashboard.</h3>
<div>
    <a href="dashboard/change">Change Password</a> <br>
    <a href="/dashboard/create">Create New Link</a>
    
</div>

@if (isset($userLinks[0]))
<table class="table ">
    <tr>
        <th scope="col">Short Link</th>
        <th scope="col">Original Link</th>
        <th scope="col">Manage Link</th>
    </tr>
    @foreach ($userLinks as $item)
        <tr scope="row">
            <td><a href="/i/{{$item['shortLink']}}">shortly.io/i/{{$item['shortLink']}}</a></td>
            <td><a href="{{$item['originLink']}}">{{$item['originLink']}}</a></td>
            <td><a href="/dashboard/link/{{$item['id']}}">Manage</a></p></td>
        </tr>
    @endforeach
</table>
@else
<h4>Parece que você ainda não criou nenhum link! <br> Venha e <a href="/dashboard/create">crie seu primeiro link</a></h4>

@endif


@endsection
