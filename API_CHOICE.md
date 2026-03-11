# API Choice

- Étudiant : Rewan
- API choisie : Agify
- URL base : https://api.agify.io
- Documentation officielle : https://agify.io/

## Endpoints testés
- GET /?name=michael
- GET /?name=<random>
- GET /?name= (cas invalide)
- GET /?name=123 (type invalide)

## Hypothèses de contrat
- Code 200 attendu pour un nom valide
- Content-Type: application/json
- Champs obligatoires :
  - name : string
  - age : int | null
  - count : int
- Cas invalide → 400 ou 422 selon fournisseur (Agify renvoie 200 mais avec valeurs null → on teste la cohérence)

## Limites / rate limiting
- Pas documenté officiellement
- API très stable
- Pas de clé API

## Risques
- Valeurs nulles possibles
- Latence variable
- Pas de vraie gestion d’erreurs côté fournisseur
