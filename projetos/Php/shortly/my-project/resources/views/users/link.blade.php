@extends('layouts.app')

@section('title') dashboard @endsection

@section('content')

<h3>Manage your Link</h3>

@if (isset($link))
    @foreach ($link as $item)
        <p>Encurtado: <a href="/i/{{$item['shortLink']}}">shortly.io/i/{{$item['shortLink']}}</a>
        Original: <a href="{{$item['originLink']}}">{{$item['originLink']}}</a> </p>
        <p>Criado em: {{$item['created_at']}}</p>
        <p>Número de Acessos: {{$item['clickCount']}}</p>
        <p>Ultimo Acesso em: {{$item['updated_at']}}</p>
    @endforeach
@endif

@if (isset($osData[0]))
<table class="table">
    <tr scope="row">
        <th scope="col">Operating System</th>
        <th scope="col">Click Count</th>
    </tr>
    @foreach ($osData as $item)
    <tr scope="row">
        <td>{{$item['osType']}}</td>
        <td>{{$item['clickCount']}}</td>
    </tr>
    @endforeach
</table>
@endif

@if (isset($browserData[0]))
<table class="table">
    <tr scope="row">
        <th scope="col">Browser Type</th>
        <th scope="col">Click Count</th>
    </tr>
    @foreach ($browserData as $item)
    <tr scope="row">
        <td>{{$item['browserType']}}</td>
        <td>{{$item['clickCount']}}</td>
    </tr>
    @endforeach
</table>
@endif

<form method="POST" action="/dashboard/link/{{$item['id']}}" >
    @csrf
    <button type="button" class="btn btn-dark">
        DELETE LINK
    </button>
</form>

@endsection

