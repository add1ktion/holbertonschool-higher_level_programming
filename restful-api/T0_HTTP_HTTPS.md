## Différences HTTP vs HTTPS

HTTP : C'est un protocole non sécurisé, les données sont en texte clair. Tout le monde sur le réseau peut les lire et/ou les modifier.

HTTPS : HTTP + TLS/SSL. Ce protocole chiffre les données, authentifie le serveur à l'aide d'un certificat et protège intégrité.

| Aspect   | HTTP        | HTTPS                      |
| -------- | ----------- | -------------------------- |
| Sécurité | Aucune      | Chiffrement + Certificat.  |
| Données  | Texte clair | Chiffrées                  |

## Structure requête HTTP

```
Requête (Client → Serveur):
GET /posts HTTP/1.1          ← Méthode + Chemin + Version
Host: jsonplaceholder.typicode.com
User-Agent: Mozilla/5.0
Accept: application/json

[Corps vide pour GET]
```

```
Réponse (Serveur → Client):
HTTP/1.1 200 OK              ← Version + Code + Message
Content-Type: application/json
Content-Length: 1024

[{"id":1,"title":"sunt...","body":"quia..."}]
```

## Méthodes HTTP (4 communes)
- GET: Récupère une ressource. Ex: charger page /home ou API /users.
- ​POST: Crée/envoie données. Ex: formulaire login, POST /users.
- PUT: Remplace ressource entière. Ex: update complet PUT /users/123.
- DELETE: Supprime ressource. Ex: DELETE /posts/42.

## Codes de statut

| Code | Nom               | Description            | Scénario                                         |
| ---- | ----------------- | ---------------------- | ------------------------------------------------ |
| 200  | OK                | Succès                 | Page/API chargée developer.mozilla​               |
| 201  | Created           | Ressource créée        | Nouvel user après POST developer.mozilla​         |
| 301  | Moved Permanently | Redirection permanente | Ancien site → nouveau domaine developer.mozilla​  |
| 400  | Bad Request       | Requête invalide       | JSON malformé developer.mozilla​                  |
| 401  | Unauthorized      | Auth requise           | Token manquant developer.mozilla​                 |
| 403  | Forbidden         | Pas de droits          | User non admin sur /admin developer.mozilla​      |
| 404  | Not Found         | Ressource inexistante  | URL fausse developer.mozilla​                     |
| 500  | Server Error      | Erreur serveur         | Bug backend/DB developer.mozilla​                 |