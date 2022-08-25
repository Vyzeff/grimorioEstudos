<?php

namespace App\Models;

use DateTimeImmutable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

use Lcobucci\JWT\Configuration;
use Lcobucci\JWT\Signer;
use Lcobucci\JWT\Signer\Key\InMemory;
use Lcobucci\JWT\Validation\Constraint\PermittedFor;
use Lcobucci\JWT\Validation\Constraint\SignedWith;
use Lcobucci\JWT\Validation\RequiredConstraintsViolated;

class JwtHandler extends Model
{
    use HasFactory;

    public function newJwtToken($username, $id, $accType = 1)
    {
        $jwtConfiguration = Configuration::forAsymmetricSigner(
            // You may use RSA or ECDSA and all their variations (256, 384, and 512) and EdDSA over Curve25519
            new Signer\Hmac\Sha256(),
            //private
            InMemory::plainText('SECRETKEY'),
            //public
            InMemory::plainText('SHORTLYKEY'),
            // You may also override the JOSE encoder/decoder if needed by providing extra arguments here
        );

        $config = $jwtConfiguration;
        assert($config instanceof Configuration);
        $now = new DateTimeImmutable();
        $token = $config->builder()
            // Configures the issuer (iss claim)
            //->issuedBy('http://shortly.io')
            // Configures the audience (aud claim)
            //->permittedFor('http://shortly.io')
            // Configures the id (jti claim)
            //->identifiedBy('4f1g23a12aa')
            // Configures the time that the token was issue (iat claim)
            ->issuedAt($now)
            // Configures the time that the token can be used (nbf claim)
            ->canOnlyBeUsedAfter($now)
            // Configures the expiration time of the token (exp claim)
            ->expiresAt($now->modify('+1 hour'))
            // Configures a new claim, payload
            ->withClaim('username', $username)
            ->withClaim('id', $id)
            ->withClaim('accType', $accType)
            // Configures a new header, called "shortly"
            ->withHeader('shortly', '0.1')
            // Builds a new token
            ->getToken($config->signer(), $config->signingKey());

        return $token;
    }

    public function validateToken($data)
    {
        $jwtConfiguration = Configuration::forAsymmetricSigner(
            // You may use RSA or ECDSA and all their variations (256, 384, and 512) and EdDSA over Curve25519
            new Signer\Hmac\Sha256(),
            //private
            InMemory::plainText('SECRETKEY'),
            //public
            InMemory::plainText('SHORTLYKEY'),
            // You may also override the JOSE encoder/decoder if needed by providing extra arguments here
        );

        $config = $jwtConfiguration;
        assert($config instanceof Configuration);
        $config->setValidationConstraints(new SignedWith(new Signer\Hmac\Sha256(), InMemory::plainText('SECRETKEY')));

        $token = $config->parser()->parse($data);
        $constraints = $config->validationConstraints();

        try {
            $config->validator()->assert($token, ...$constraints);
        } catch (RequiredConstraintsViolated $e) {
            // list of constraints violation exceptions:
            return $e;
        }
        return 0;
    }

    public function parseToken($data)
    {
        $jwtConfiguration = Configuration::forAsymmetricSigner(
            // You may use RSA or ECDSA and all their variations (256, 384, and 512) and EdDSA over Curve25519
            new Signer\Hmac\Sha256(),
            //private
            InMemory::plainText('SECRETKEY'),
            //public
            InMemory::plainText('SHORTLYKEY'),
            // You may also override the JOSE encoder/decoder if needed by providing extra arguments here
        );

        $config = $jwtConfiguration;
        assert($config instanceof Configuration);

        $token = $config->parser()->parse($data);
        return $token;
    }
}
