# Despliegue en GitHub Pages con dominio www.aggoacountt.com

Esta guía cubre los **3 pasos** para publicar el sitio: registrar el dominio, subirlo a GitHub y configurar el DNS.

---

## ✅ Lo que ya está listo

- ✔ Repositorio Git inicializado con el primer commit hecho.
- ✔ Archivo `CNAME` creado con `www.aggoacountt.com`.
- ✔ `README.md`, `.gitignore` y guía de edición incluidos.

---

## PASO 1 — Registrar el dominio aggoacountt.com

Como `.com` es un dominio internacional, necesita un registrador. Recomendaciones:

| Registrador | Precio aprox. /año | Notas |
|---|---|---|
| **Namecheap** (https://www.namecheap.com) | ~$10–12 USD | El más usado, panel sencillo |
| **Cloudflare** (https://www.cloudflare.com/products/registrar/) | ~$9.15 USD | Precio al costo + DNS gratuito |
| **GoDaddy** (https://www.godaddy.com) | ~$12–20 USD | Más caro pero conocido |
| **NIC.EC** | — | Solo dominios `.ec`. Si prefiere `aggoacountt.ec`, use este. |

> 💡 **Recomendación:** Cloudflare es el más barato y rápido para configurar DNS.

**Acciones:**
1. Busque `aggoacountt.com` en el registrador elegido.
2. Cómprelo (1 año mínimo, ideal 2-3 años).
3. **Guarde el acceso al panel DNS** — lo necesitará en el Paso 3.

---

## PASO 2 — Subir el sitio a GitHub

### 2.1 — Crear cuenta y repositorio

1. Entre a https://github.com y cree una cuenta (use el correo `aggo.acountt@gmail.com` o uno corporativo).
2. Haga clic en **+ → New repository**.
3. Configure así:
   - **Repository name:** `aggo-associates` (o cualquier nombre)
   - **Public** ✅ (debe ser público para usar GitHub Pages gratis)
   - **NO** marque "Add a README", "Add .gitignore", ni licencia (ya los tenemos).
4. Clic en **Create repository**.

### 2.2 — Conectar y subir desde su computadora

GitHub le mostrará comandos. Use los siguientes (reemplace `SUUSUARIO` por su nombre de usuario real de GitHub):

Abra **PowerShell** o **Git Bash** y ejecute:

```bash
cd "C:/Users/ADMIN/Desktop/Tareas/PROGRAMAS/16. aggo-associates"
git remote add origin https://github.com/SUUSUARIO/aggo-associates.git
git push -u origin main
```

GitHub le pedirá iniciar sesión. La primera vez recomendamos usar **GitHub CLI** (`gh auth login`) o un **Personal Access Token** en lugar de contraseña.

### 2.3 — Activar GitHub Pages

1. En su repositorio en github.com → pestaña **Settings**.
2. Menú izquierdo → **Pages**.
3. En **Source**, elija **Deploy from a branch**.
4. **Branch:** `main` — **Folder:** `/ (root)`. Clic en **Save**.
5. Espere 1-2 minutos. Aparecerá un mensaje verde: *"Your site is live at https://suusuario.github.io/aggo-associates/"*

### 2.4 — Configurar el dominio personalizado en GitHub

1. En la misma página **Settings → Pages**.
2. En **Custom domain**, escriba: `www.aggoacountt.com`
3. Clic en **Save**.
4. Marque ✅ **Enforce HTTPS** (espere 10-30 min a que GitHub emita el certificado SSL gratuito).

---

## PASO 3 — Configurar DNS en su registrador

Vaya al panel DNS de su dominio (Namecheap → "Advanced DNS", Cloudflare → "DNS Records", etc.) y agregue estos registros:

### Registros A (para el dominio raíz `aggoacountt.com`)

| Tipo | Host / Nombre | Valor | TTL |
|------|---|---|---|
| A | `@` | `185.199.108.153` | Auto |
| A | `@` | `185.199.109.153` | Auto |
| A | `@` | `185.199.110.153` | Auto |
| A | `@` | `185.199.111.153` | Auto |

### Registro CNAME (para `www`)

| Tipo | Host / Nombre | Valor | TTL |
|------|---|---|---|
| CNAME | `www` | `SUUSUARIO.github.io` | Auto |

> ⚠️ Reemplace `SUUSUARIO` por su usuario real de GitHub. **No ponga `https://` ni `/`**, solo `suusuario.github.io`.

### Si usa Cloudflare específicamente

- Cuando agregue los registros A, ponga la nube en **gris (DNS only)** las primeras 24-48 horas; luego puede activarla en naranja para CDN.

---

## Tiempos de propagación

- **DNS:** 15 minutos a 24 horas (normal: 1-2 horas).
- **Certificado HTTPS de GitHub:** 10-30 minutos después de verificar el dominio.
- Pruebe en https://www.aggoacountt.com — si no carga aún, espere e intente desde un navegador en modo incógnito.

---

## ✏️ Cómo editar el sitio después del despliegue

### Opción rápida (desde GitHub, sin instalar nada)
1. Entre a su repo en github.com.
2. Clic en `index.html`.
3. Clic en el ícono de **lápiz** (✏️ Edit).
4. Modifique el texto.
5. Abajo, clic en **Commit changes**.
6. En 1-2 minutos los cambios estarán en vivo en www.aggoacountt.com.

### Opción local (recomendada para cambios grandes)
1. Edite `index.html` con VS Code o el Bloc de Notas.
2. En la terminal:
   ```bash
   cd "C:/Users/ADMIN/Desktop/Tareas/PROGRAMAS/16. aggo-associates"
   git add .
   git commit -m "Descripción del cambio"
   git push
   ```

---

## ❓ Problemas comunes

**El dominio no carga después de 24h.**
→ Revise en Settings → Pages si el "DNS check" sale verde. Verifique que los registros A apunten a las 4 IPs correctas de GitHub.

**Error: "Domain is not properly configured"**
→ Espere más tiempo. Si persiste, elimine el dominio en Settings → Pages, guarde, y vuelva a agregarlo.

**El formulario de contacto no envía mensajes.**
→ GitHub Pages **no procesa formularios**. Tiene 3 alternativas:
1. **Formspree** (https://formspree.io) — gratis hasta 50 mensajes/mes. Solo cambie `<form>` para incluir `action="https://formspree.io/f/SUID"`.
2. **Web3Forms** (https://web3forms.com) — gratis e ilimitado, similar configuración.
3. **EmailJS** — envía a su Gmail directamente.

Si necesita ayuda con esto, puedo prepararlo cuando me indique.

---

## Resumen

| Paso | Acción | Dónde |
|---|---|---|
| 1 | Comprar `aggoacountt.com` | Namecheap / Cloudflare |
| 2 | Crear repo y `git push` | github.com |
| 3 | Activar Pages + dominio custom | GitHub → Settings → Pages |
| 4 | Configurar DNS (4 A + 1 CNAME) | Panel del registrador |
| 5 | Esperar propagación | — |
| 6 | Listo: https://www.aggoacountt.com | 🎉 |
