@extends('layouts.app')

@section('title') dashboard @endsection

@section('content')

<div><h3>Create a new link below!</h3></div>
<div>
    <form method="POST" action="/dashboard/create">
        @csrf
        <div>
            <!-- LINK Address -->
            <div><p>Seu Link</p></div>
            <div>
                <input id="link" class="" name="link" required autofocus placeholder="Your Link Here" />
            </div>
            <div><p>Como você quer que fique depois de <em>shortly.io/i/</em>? <br> Deixe em branco para uma finalização aleatória.</p></div>
            <div>
                <input id="customChunk" class="" name="customChunk"  placeholder="Your Brand Here" />
            </div>
            <button class="btn btn-dark" type="submit">
                CREATE
            </button>
        </div>
    </form>
</div>
@endsection

