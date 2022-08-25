<?php

namespace App\Http\Controllers;

use App\Models\DataCollector;
use App\Models\JwtHandler;
use App\Models\Links;

class collectController extends Controller
{
    public function firstCollect($link)
    {
        //RETRIEVE ORIGIN LINK
        $shortLink = $link;
        $linkManager = new Links();
        $linkId = $linkManager->getLinkShort($shortLink);

        //COLLECT DATA

        $dataManager = new DataCollector();
        $dataManager->totalCheckup($linkId);

        $redirectTo = $linkManager->redirectLink($shortLink);

        return redirect($redirectTo);
    }
}
