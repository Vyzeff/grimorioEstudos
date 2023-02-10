@if (isset($data))
{{$data}} 
@else
<h4>There was an error, please try again.</h4>
@endif

@if (isset($error))
    <h4>There was an error with your request:</h4>
    <p>{{$error}}</p>
@endif