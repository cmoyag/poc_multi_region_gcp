## Poc en GCP para Validar una arquitectura Activa / Pavisa con recursos serverless (Cloud Run)
**Pasos a Seguir:**
1. Ingresar a la consola de GCP
2. Habilitar la consola CLI y Crear variable 
      - export GOOGLE_CLOUD_PROJECT_SF= [id proyecto] 
      - export NAME_IMAGEN_A = poc-multiregion-backend-us-east-1
      - export NAME_IMAGEN_B = poc-multiregion-backend-us-central-1
3. Descargar el repositorio
4. Compilar la Imagen Docker  gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT_SF}/[nombre imagen]
5. Compilar la Cloud run :
<code>
gcloud run deploy ${GOOGLE_CLOUD_PROJECT_SF}
--image gcr.io/${GOOGLE_CLOUD_PROJECT_SF}/${NAME_IMAGEN_A}:v1 --memory=128mi --port=3000 --region=us-east1
</code>
<code>
gcloud run deploy ${GOOGLE_CLOUD_PROJECT_SF}
--image gcr.io/${GOOGLE_CLOUD_PROJECT_SF}/${NAME_IMAGEN_B}:v1 --memory=128mi --port=3000 --region=us-central1
</code>
