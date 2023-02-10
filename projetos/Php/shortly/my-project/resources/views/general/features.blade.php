@extends('layouts.app')

@section('title') Features @endsection

@section('content')
<div>
    <h2 class="pageheader">The complete solution to link management</h2>
    <h4>From link to team management,<mark>everything</mark>  you need is here!</h4>
</div>
<div class="featuresall">
    <div class="featuresdisplay">
        <div class="featuresitem dropdown" data-dropdown="1">
            <h5>Custom Link Names</h5>
            <p data-content="1" class="hidden dropdown-content">
                Choose the latter part of a link to whichever 7 letter text you may want. Go crazy!
            </p>
        </div>
        <div class="featuresitem dropdown" data-dropdown="5">
            <h5>API Integration</h5>
            <p data-content="5" class="hidden dropdown-content">
                Create custom tokens that collect your data for you!
            </p>
        </div>
        <div class="featuresitem dropdown" data-dropdown="3">
            <h5>Account Management</h5>
            <p data-content="3" class="hidden dropdown-content">
                Manage your and your team's accounts with our robust moderation features
            </p>
        </div>
    </div>
    <div class="featuresdisplay" id="featuresleft">
        <div class="featuresitem dropdown" data-dropdown="2">
            <h5>Branding</h5>
            <p data-content="2" class="hidden dropdown-content">
                Your links will now carry your brand with you, making marketing so much easier to handle with patented links
            </p>
        </div>
        <div class="featuresitem dropdown" data-dropdown="4">
            <h5>Analysis Tools</h5>
            <p data-content="4" class="hidden dropdown-content">
                Analyse your link's success with our various tools focused on helping making your job easier, from browser to operating system detection, and much more!
            </p>
        </div>
        <div class="featuresitem dropdown" data-dropdown="6">
            <h5>Faster redirects</h5>
            <p data-content="6" class="hidden dropdown-content">
                Even under high loads, our capable servers will earn you smoother redirects than anywhere else
            </p>
        </div>
    </div>
</div>

<div>
    <h3>24/7 Support</h3>
    <p>
        Got a problem? Have a talk with our amazing <a href="/help">support team</a>  or skim through our <a href="/">documentation</a>
        for a more in depth experience.
    </p>
</div>
@endsection

