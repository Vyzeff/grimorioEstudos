<?php

namespace App\Models;

use DateTimeImmutable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

use Lcobucci\JWT\Configuration;
use Lcobucci\JWT\Signer;
use Lcobucci\JWT\Signer\Key\InMemory;
use Lcobucci\JWT\Validation\Constraint\SignedWith;
use Lcobucci\JWT\Validation\RequiredConstraintsViolated;

class JwtHandler extends Model
{
    use HasFactory;

    // taken directly from the jwt website instructions
    // I dont think it is properly spaced, but I will leave as it is
    public function newJwtToken($username, $id, $accType = 1)
    {
        $jwtConfiguration = Configuration::forAsymmetricSigner(
            // You may use RSA or ECDSA and all their variations (256, 384, and 512) and EdDSA over Curve25519
            new Signer\Hmac\Sha256(),
            //private key
            InMemory::plainText('SECRETKEY'),
            //public key
            InMemory::plainText('SHORTLYKEY'),
            // You may also override the JOSE encoder/decoder if needed by providing extra arguments here
        );

        $config = $jwtConfiguration;
        assert($config instanceof Configuration);
        $now = new DateTimeImmutable();
        $token = $config->builder()
            // Configures the issuer (iss claim)
            // this would be used if the app where running on a actual server, but
            // on localhost it only breaks things
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
            // this is basically what I modified, the data that actually goes into the session
            ->withClaim('username', $username)
            ->withClaim('id', $id)
            ->withClaim('accType', $accType)
            // Configures a new header, called "shortly"
            ->withHeader('shortly', '0.1')
            // Builds a new token
            ->getToken($config->signer(), $config->signingKey());

        return $token;
    }

    // simply validates a given token, I couldn't get it working without slaping the whole
    // configuration on the go, so it is ugly, but it works.
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

        // the validations that the function will run the token against, right now it simply
        // requires the keys to be correct, but I think that it auto checks for expiration date
        $config = $jwtConfiguration;
        assert($config instanceof Configuration);
        $config->setValidationConstraints(new SignedWith(
            new Signer\Hmac\Sha256(),
            InMemory::plainText('SECRETKEY')
        ));

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

    // parses the token from plain text to a jwt object from what I get
    // same issue to, I couldn't get it to work without the full config on function
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
    public function newApiToken($id)
    {
        $jwtConfiguration = Configuration::forAsymmetricSigner(
            // You may use RSA or ECDSA and all their variations (256, 384, and 512) and EdDSA over Curve25519
            new Signer\Hmac\Sha256(),
            //private key
            InMemory::plainText('SECRETKEY'),
            //public key
            InMemory::plainText('SHORTLYKEY'),
            // You may also override the JOSE encoder/decoder if needed by providing extra arguments here
        );

        $config = $jwtConfiguration;
        assert($config instanceof Configuration);
        $now = new DateTimeImmutable();
        $token = $config->builder()
            // Configures the issuer (iss claim)
            // this would be used if the app where running on a actual server, but
            // on localhost it only breaks things
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
            ->expiresAt($now->modify('+24 hour'))
            // Configures a new claim, payload
            // this is basically what I modified, the data that actually goes into the session
            ->withClaim('id', $id)
            // Configures a new header, called "shortly"
            ->withHeader('shortly', '0.1')
            // Builds a new token
            ->getToken($config->signer(), $config->signingKey());

        return $token;
    }
}
