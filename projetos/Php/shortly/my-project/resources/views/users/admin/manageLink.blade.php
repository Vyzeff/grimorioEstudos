@extends('layouts.app')

@section('title') staff @endsection

@section('content')

<h3>Manage a Link</h3>

@if (isset($link))
    @foreach ($link as $item)
        <p>Criado Por Usuario de Id {{$item['userId']}}</p>
        <p>Encurtado: <a href="/i/{{$item['shortLink']}}">shortly.io/i/{{$item['shortLink']}}</a>
        Original: <a href="{{$item['originLink']}}">{{$item['originLink']}}</a> </p>
        <p>Criado em: {{$item['created_at']}}</p>
        <p>Número de Acessos: {{$item['clickCount']}}</p>
        <p>Ultimo Acesso em: {{$item['updated_at']}}</p>

    @endforeach
@endif

@if (isset($osData[0]))
<table>
    <tr>
        <th>Operating System</th>
        <th>Click Count</th>
    </tr>
    @foreach ($osData as $item)
    <tr>
        <td>{{$item['osType']}}</td>
        <td>{{$item['clickCount']}}</td>
    </tr>
    @endforeach
</table>
@endif

@if (isset($browserData[0]))
<table>
    <tr>
        <th>Browser Type</th>
        <th>Click Count</th>
    </tr>
    @foreach ($browserData as $item)
    <tr>
        <td>{{$item['browserType']}}</td>
        <td>{{$item['clickCount']}}</td>
    </tr>
    @endforeach
</table>
@endif

<form method="POST" action="/staff/links/{{$item['id']}}" >
    @csrf
    <button class="btn btn-dark" type="button">
        DELETE LINK
    </button>
</form>

@endsection

