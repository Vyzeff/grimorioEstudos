@extends('layouts.app')

@section('title') api @endsection

@section('content')


<h2>API</h2>
<p>API</p>

<form method="POST" action="/token">
            @csrf

            <!-- LINK Address -->
            <div>
                <input id="apitoken" class="" name="apitoken" required placeholder="Your Token Here" />
            </div>
                <button class="ml-3">
                    GET API
                </button>
            </div>
</form>



@endsection
