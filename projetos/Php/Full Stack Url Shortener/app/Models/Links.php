<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class Links extends Model
{
    use HasFactory;
    /**
     * Show the profile for the given user.
     *
     * @param  Request  $request
     *
     *
     */
    protected $fillable = [
        'userId',
        'originLink',
        'shortLink',
        'clickCount',
    ];

    protected function createLink($finalChunk, $input, $id = 1)
    {
        Links::create([
            'userId' => $id,
            'originLink' => $input,
            'shortLink' => $finalChunk,
            'clickCount' => '0',
        ]);
        return 0;
    }

    protected function generateRandomString($length = 10)
    {
        $characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $charactersLength = strlen($characters);
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, $charactersLength - 1)];
        }
        return $randomString;
    }

    public function checkLink($input, $id, $customChunk = null)
    {
        if ($customChunk == null) {
            $randChunk = $this->generateRandomString(7);
            $this->createLink($randChunk, $input, $id);
            return $randChunk;
        } else {
            $this->createLink($customChunk, $input, $id);
            return $customChunk;
        }
    }

    public function redirectLink($shortLink)
    {
        $rawQuery = DB::table('links')->select(['originLink'])->where('shortLink', '=', "$shortLink")->get();
        $query = json_decode(json_encode($rawQuery), true);
        return $query[0]['originLink'];
    }

    public function getLink($id)
    {

        $rawQuery = DB::select("SELECT * FROM links WHERE id = '{$id}'");
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }

    public function getAllLinks($id = 0)
    {
        if ($id == 0) {
            $rawQuery = Links::all();
            $query = json_decode(json_encode($rawQuery), true);

            return $query;
        }
        $rawQuery = DB::select("SELECT id, shortLink, originLink FROM links WHERE userId = '{$id}'");
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }

    public function deleteLink($id)
    {
        DB::table('osData')->where('linkId', '=', $id)->delete();
        DB::table('browserData')->where('linkId', '=', $id)->delete();
        Links::destroy($id);
        return 0;
    }

    public function getLinkShort($shortLink)
    {
        $rawQuery = DB::table('links')->select(['id'])->where('shortLink', '=', "$shortLink")->get();
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }
}
