# Guía de Publicación y Edición — AGGO Associates C.A.

## 1. Estructura del sitio

```
16. aggo-associates/
├── index.html          ← Toda la página web (HTML + CSS + JS)
└── GUIA-PUBLICACION.md ← Este documento
```

Es un sitio **estático de un solo archivo**, sin dependencias ni base de datos.
Funciona con doble clic, en cualquier hosting, y carga rápido en cualquier dispositivo.

---

## 2. Cómo lanzar el sitio (3 opciones, de más fácil a más profesional)

### Opción A — Netlify Drop (RECOMENDADA, gratis, 2 minutos)

1. Entre a https://app.netlify.com/drop
2. Arrastre la carpeta `16. aggo-associates` completa al recuadro.
3. Listo. Netlify le dará una URL pública del tipo `aggo-associates.netlify.app`.
4. **El formulario de contacto funcionará automáticamente** — los mensajes llegarán al panel de Netlify y a su correo.
5. Para conectar un dominio propio (ej. `aggoassociates.ec`), use **Domain Settings** dentro de Netlify.

**Editar después:** vuelve a `app.netlify.com/drop` y arrastra la carpeta actualizada. O conecte un repositorio Git para edición continua.

---

### Opción B — GitHub Pages (gratis, requiere cuenta GitHub)

1. Cree una cuenta en https://github.com
2. Cree un repositorio nuevo llamado `aggo-associates`.
3. Suba el archivo `index.html`.
4. En **Settings → Pages**, active **Deploy from branch: main**.
5. URL pública: `https://[suusuario].github.io/aggo-associates`.

**Editar después:** modifique `index.html` desde la propia web de GitHub (botón del lápiz) → Commit → se publica en 1 minuto.

---

### Opción C — Hosting tradicional con dominio propio

Si ya tiene un hosting (Hostinger, GoDaddy, NIC.ec, etc.):
1. Acceda al **cPanel** o gestor de archivos.
2. Suba `index.html` a la carpeta `public_html/` o `www/`.
3. El sitio queda accesible en su dominio.

Para registrar un dominio `.ec` en Ecuador: https://nic.ec
Sugerencias de dominio:
- `aggoassociates.ec`
- `aggoassociates.com`
- `aggo.ec`

---

## 3. Cómo editar contenido sin programar

Abra `index.html` con el **Bloc de Notas**, **Notepad++** o **VS Code** y use Buscar (Ctrl+F).

### Datos de contacto

| Quiere cambiar... | Busque este texto |
|---|---|
| Teléfono visible | `+593 99 107 1743` |
| Enlace de teléfono | `+593991071743` |
| Correo electrónico | `aggo.acountt@gmail.com` |
| Dirección | `C.C. Oro Plaza, Local 212` |
| Mensaje WhatsApp pre-cargado | `Hola%20AGGO%20Associates` |

### Textos principales

| Sección | Cómo encontrarla |
|---|---|
| Título del hero | `AGGO Associates` (línea con `class="hero-title"`) |
| Subtítulo / tagline | `Acompañamos a su empresa` |
| Quiénes Somos | `<section class="about"` |
| Servicios principales (4) | `<section class="services"` |
| Servicios especializados | `<!-- ===== Servicios Especializados =====` |
| Sector minero | `<!-- ============ SECTORS ===========` |
| Proceso de trabajo | `<!-- ============ PROCESS ===========` |

### Estadísticas del hero (años, clientes…)

Busque `hero-stats` y modifique los números:
```html
<div class="stat"><div class="n">+15</div><div class="l">Años Exp.</div></div>
```

### Agregar o quitar un sub-servicio

Cada ítem es una línea `<li>...</li>` dentro de `<ul class="service-list">`. Cópielo y modifíquelo.

### Cambiar colores corporativos

Al inicio del `<style>` (línea ~10), modifique las variables:
```css
--navy-800:#0a1830;   /* azul marino principal */
--gold:#c9a35c;       /* dorado */
--gold-light:#e6c585; /* dorado claro */
```

---

## 4. Reemplazar el logo SVG por su logo real (opcional)

Si quiere usar la imagen de su logo en lugar del SVG generado:

1. Coloque su logo (PNG con fondo transparente, mínimo 400×400 px) en la misma carpeta como `logo.png`.
2. Busque `<div class="hero-logo">` y reemplace el `<svg>...</svg>` interior por:
   ```html
   <img src="logo.png" alt="AGGO Associates" style="width:100%;height:100%;object-fit:contain;border-radius:50%">
   ```
3. Igual para el logo del navbar y footer si lo desea.

---

## 5. Recomendaciones a futuro

- **Google Analytics** — Para medir visitas: cree cuenta en https://analytics.google.com y agregue el script antes de `</head>`.
- **Google Business** — Registre su oficina en Google Maps: https://business.google.com (esencial para que aparezca al buscar "contador Machala").
- **SEO local** — Agregue palabras clave como *contador Machala*, *auditoría El Oro*, *peritaje contable Ecuador*, *firma contable minería* en los textos.
- **Blog / Noticias** — Si quiere publicar artículos de actualidad fiscal, conviene migrar a una plataforma con CMS (WordPress, Webflow). El sitio actual es ideal para una landing institucional.
- **Backup** — Guarde una copia del archivo `index.html` en Google Drive o Dropbox cada vez que lo edite.

---

## 6. Soporte

Para cualquier modificación mayor (agregar páginas, integrar formularios avanzados, blog, área de clientes), conserve este archivo como referencia de la estructura original.

**Última actualización:** Mayo 2026
