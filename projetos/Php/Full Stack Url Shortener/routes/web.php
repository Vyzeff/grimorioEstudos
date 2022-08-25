<?php

use App\Http\Controllers\authController;
use App\Http\Controllers\collectController;
use App\Http\Controllers\homeController;
use App\Http\Controllers\redirectController;
use App\Http\Controllers\staffController;
use App\Http\Controllers\userController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', [homeController::class, 'index']);
Route::post('/', [homeController::class, 'link']);
Route::get('/features', [homeController::class, 'features']);
Route::get('/help', [homeController::class, 'help']);


Route::match((['get', 'post']), '/login', [authController::class, 'loginChoose']);
Route::match((['get', 'post']), '/register', [authController::class, 'registerChoose']);
Route::match((['get', 'post']), '/dashboard/change', [authController::class, 'userChange']);
Route::get('/logout', [authController::class, 'logout']);


Route::get('/dashboard/', [userController::class, 'dashboard']);
Route::match((['get', 'post']), '/dashboard/create', [userController::class, 'userLink']);
Route::match((['get', 'post']), '/dashboard/link/{id}', [userController::class, 'manageLink']);


Route::get('/staff', [staffController::class, 'staffDash']);
Route::get('/staff/users', [staffController::class, 'staffUsers']);
Route::get('/staff/links', [staffController::class, 'staffLinks']);
Route::match((['get', 'post']), '/staff/users/create', [staffController::class, 'staffCreate']);
Route::match((['get', 'post']), 'staff/links/{id}', [staffController::class, 'manageLink']);
Route::match((['get', 'post']), 'staff/users/{id}', [staffController::class, 'manageUsers']);
Route::match((['get', 'post']), '/staff/change', [staffController::class, 'staffChange']);

Route::get('/i/{link}', [collectController::class, 'firstCollect']);
