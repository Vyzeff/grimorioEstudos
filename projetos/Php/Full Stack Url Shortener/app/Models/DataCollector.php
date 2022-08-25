<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\DB;

class DataCollector extends Model
{
    use HasFactory;


    protected function getBrowser()
    {
        $info = $_SERVER['HTTP_USER_AGENT'];
        if (strpos($info, 'MSIE') !== false)
            return 'Internet explorer';
        elseif (strpos($info, 'Trident') !== false)
            return 'Internet explorer';
        elseif (strpos($info, 'Firefox') !== false)
            return 'Mozilla Firefox';
        elseif (strpos($info, 'Chrome') !== false)
            return 'Google Chrome';
        elseif (strpos($info, 'Opera Mini') !== false)
            return "Opera Mini";
        elseif (strpos($info, 'Opera') !== false)
            return "Opera";
        elseif (strpos($info, 'Safari') !== false)
            return "Safari";
        else
            return 'Other';
    }

    protected function getOS()
    {
        $info = $_SERVER['HTTP_USER_AGENT'];
        $os = "";

        if (strpos($info, 'Linux') !== false) {
            $os .= 'Linux';
        } elseif (strpos($info, 'macintosh') !== false) {
            $os .= 'Mac OS';
        } elseif (strpos($info, 'mac os x') !== false) {
            $os .= 'Mac OS';
        } elseif (strpos($info, 'mac_powerpc') !== false) {
            $os .= 'Mac OS';
        } elseif (strpos($info, 'windows') !== false) {
            $os .= "Windows";
        } elseif (strpos($info, 'win') !== false) {
            $os .= "Windows";
        } elseif (strpos($info, 'ubuntu') !== false) {
            $os .= "Ubuntu";
        } elseif (strpos($info, 'iphone') !== false) {
            $os .= "Iphone";
        } elseif (strpos($info, 'android') !== false) {
            $os .= "Android";
        } elseif (strpos($info, 'blackberry') !== false) {
            $os .= "Blackberry";
        } elseif (strpos($info, 'webos') !== false) {
            $os .= "Other Mobile";
        } else {
            $os .= 'Other';
        }
        return $os;
    }

    public function getBrowserData($id)
    {
        $rawData = DB::table('browserData')->where('linkId', '=', $id)->get();
        $data = json_decode(json_encode($rawData), true);
        return $data;
    }

    public function getOsData($id)
    {
        $rawData = DB::table('osData')->where('linkId', '=', $id)->get();
        $data = json_decode(json_encode($rawData), true);
        return $data;
    }

    public function totalCheckup($linkId)
    {
        $dateNow = date("Y-m-d H:i:s");
        DB::table('links')->where('id', '=', $linkId[0]['id'])->update(['updated_at' => $dateNow]);
        DB::table('links')->where('id', '=', $linkId[0]['id'])->increment('clickCount', 1);

        $browser = $this->getBrowser();
        $os = $this->getOS();

        //browser update
        $rawQuery = DB::table('browserData')->select('clickCount')->where('browserType', '=', "$browser")->where('linkId', '=', $linkId)->get();
        $query = json_decode(json_encode($rawQuery), true);
        if (isset($query[0])) {
            DB::table('browserData')->where('browserType', '=', "$browser")->where('linkId', '=', $linkId)->increment('clickCount', '1');
        } else {
            DB::table('browserData')->updateOrInsert(['linkId' => "$linkId[0]['id']", 'browserType' => "$browser"], ['clickCount' => '0']);
            DB::table('browserData')->where('browserType', '=', "$browser")->where('linkId', '=', "$linkId")->increment('clickCount', '1');
        }

        //os update
        $rawQuery1 = DB::table('osData')->select('clickCount')->where('osType', '=', "$os")->where('linkId', '=', $linkId)->get();
        $query1 = json_decode(json_encode($rawQuery1), true);
        if (isset($query1[0])) {
            DB::table('osData')->where('osType', '=', "$os")->where('linkId', '=', $linkId)->increment('clickCount', '1');
        } else {
            DB::table('osData')->updateOrInsert(['linkId' => $linkId[0]['id'], 'osType' => "$os"], ['clickCount' => '0']);
            DB::table('osData')->where('osType', '=', "$os")->where('linkId', '=', $linkId)->increment('clickCount', '1');
        }
        return 0;
    }
}
