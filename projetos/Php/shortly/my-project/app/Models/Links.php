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

    // creates a link based on a original input, a user id default to admin00, and a final chunk
    // which is either a custom generated string or some user input
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

    // generates a random string to use when there is no custom input from user
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

    // link validation if I get around to it, for now it basically only checks if there is
    // a custom input from the user
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

    // returns the original link based on the final chunk of a shortLink
    public function redirectLink($shortLink)
    {
        $rawQuery = DB::table('links')->select(['originLink'])->where('shortLink', '=', "$shortLink")->get();
        $query = json_decode(json_encode($rawQuery), true);
        return $query[0]['originLink'];
    }

    // gets everything from a link based on its unique id
    public function getLink($id)
    {

        $rawQuery = DB::table('links')->select()->where('id', '=', "{$id}")->get();
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }

    // gets all links, admin only
    public function getAllLinks($id = 0)
    {
        if ($id == 0) {
            $rawQuery = Links::all();
            $query = json_decode(json_encode($rawQuery), true);

            return $query;
        }
        $rawQuery = DB::select("SELECT * FROM links WHERE userId = '{$id}'");
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }

    // deletes a link and all of its footprints on other dbs
    // both user and admin have access to it
    public function deleteLink($id)
    {
        DB::table('osData')->where('linkId', '=', $id)->delete();
        DB::table('browserData')->where('linkId', '=', $id)->delete();
        Links::destroy($id);
        return 0;
    }

    // gets a link id based on its final chunk
    public function getLinkShort($shortLink)
    {
        $rawQuery = DB::table('links')->select(['id'])->where('shortLink', '=', "$shortLink")->get();
        $query = json_decode(json_encode($rawQuery), true);

        return $query;
    }
}
