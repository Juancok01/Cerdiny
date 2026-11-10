(function () {
  const P = window.PERFIL;
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => `&#${c.charCodeAt(0)};`);

  // Logos en img/icons/<id>.svg. Para una herramienta nueva, agrega su archivo y su nombre aquí.
  const LOGOS = {
    sql: "SQL",
    postgres: "PostgreSQL",
    mysql: "MySQL",
    python: "Python",
    pandas: "pandas",
    etl: "Pipelines ETL/ELT",
    athena: "AWS Athena",
    bigquery: "BigQuery",
    quicksight: "Amazon QuickSight",
    looker: "Looker Studio",
    shiny: "R Shiny",
    excel: "Microsoft Excel",
  };
  const tile = (id) => LOGOS[id]
    ? `<span class="tile" title="${esc(LOGOS[id])}"><img src="img/icons/${esc(id)}.svg" alt="${esc(LOGOS[id])}" /></span>`
    : `<span class="tile" title="${esc(id)}">${esc(id.slice(0, 2).toUpperCase())}</span>`;

  const ICONOS = {
    proyecto: '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    migracion: '<ellipse cx="12" cy="5.500" rx="8" ry="3"/><path d="M4 5.500v13c0 1.700 3.600 3 8 3s8-1.300 8-3v-13M4 12c0 1.700 3.600 3 8 3s8-1.300 8-3"/>',
    tabla: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M3 15h18M9 10v10"/>',
    reloj: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    github: '<path d="M9 19c-4 1.300-4-2-6-2.500M15 21v-3.500a3 3 0 0 0-.9-2.400c3-.3 6-1.500 6-6.500a5 5 0 0 0-1.400-3.500 4.600 4.600 0 0 0-.1-3.500s-1.100-.3-3.600 1.400a12.300 12.300 0 0 0-6.500 0C6 1.300 4.900 1.600 4.900 1.600a4.600 4.600 0 0 0-.1 3.500A5 5 0 0 0 3.400 8.600c0 5 3 6.200 6 6.500a3 3 0 0 0-.9 2.400V21"/>',
    linkedin: '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-7M12 13c0-3 5-3.500 5 0v4"/>',
    email: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    telefono: '<path d="M5 3h4l2 5-2.500 1.500a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
  };
  const icon = (n) => `<svg viewBox="0 0 24 24" aria-hidden="true">${ICONOS[n] || ""}</svg>`;

  const NIVELES = { avanzado: ["Avanzado", 88], intermedio: ["Intermedio", 62], aprendiendo: ["Aprendiendo", 34] };

  const box = (x, y, w, h, t) =>
    `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="6" fill="#0b0f2e" stroke="#a78bfa" stroke-width="1.500"/>` +
    (t ? `<text x="${x + w / 2}" y="${y + h / 2 + 4}" text-anchor="middle" font-size="11" font-weight="600" fill="#e7e4ff" font-family="Segoe UI,sans-serif">${t}</text>` : "");
  const line = (d) => `<path d="${d}" fill="none" stroke="#7c5cff" stroke-width="2"/>`;
  const VISUALES = {
    pipeline: box(28, 62, 72, 46, "Postgres") + line("M100 85h24") + box(124, 62, 72, 46, "pandas") + line("M196 85h24") + box(220, 62, 72, 46, "Correo") +
      `<text x="160" y="140" text-anchor="middle" font-size="10" fill="#a5abc8" font-family="Segoe UI,sans-serif">cada 15 minutos</text>`,
    embudo: box(70, 26, 180, 34, "Visitas") + box(100, 68, 120, 34, "Categorías") + box(120, 110, 80, 34, "WhatsApp"),
    ventas: line("M100 48h60v28M100 122h60V94M160 48h60") + box(20, 30, 80, 36, "Productos") + box(20, 104, 80, 36, "Vendedores") + box(124, 68, 72, 34, "Ventas") + box(220, 30, 84, 36, "Histórico"),
    excel: box(40, 22, 72, 22, "Filtros") + box(124, 22, 156, 22, "Buscar empleado") + box(40, 54, 240, 96, "") +
      [[62, 62], [92, 44], [122, 72], [152, 36], [182, 56], [212, 28]].map(([x, h]) => `<rect x="${x}" y="${140 - h}" width="20" height="${h}" rx="2" fill="#7c5cff"/>`).join(""),
    er: line("M160 86H86M160 86h74M160 86V44M160 86v42") + box(122, 66, 76, 40, "transaccion") + box(22, 70, 64, 32, "usuarios") + box(234, 70, 64, 32, "comercio") + box(130, 16, 60, 28, "riesgo") + box(130, 128, 60, 28, "divisas"),
    seguridad: box(30, 28, 90, 30, "negocio A") + box(30, 112, 90, 30, "negocio B") + line("M120 43h40v28M120 127h40V99") +
      `<path d="M198 40l44 14v30c0 28-20 42-44 52-24-10-44-24-44-52V54z" fill="#0b0f2e" stroke="#a78bfa" stroke-width="1.500"/><text x="198" y="94" text-anchor="middle" font-size="15" font-weight="700" fill="#e7e4ff" font-family="Segoe UI,sans-serif">RLS</text>`,
    migraciones: [0, 1, 2, 3, 4].map((i) => box(36 + i * 52, 118 - i * 20, 40, 34, String(1 + i * 6).padStart(3, "0"))).join("") + line("M56 118V96M108 98V76M160 78V56M212 58V36"),
  };
  const art = (v) => `<svg viewBox="0 0 320 170" aria-hidden="true">${VISUALES[v] || ""}</svg>`;

  document.querySelectorAll("[data-nombre]").forEach((n) => (n.textContent = P.nombre));
  document.querySelector("[data-corto]").textContent = P.nombreCorto;
  $("anio").textContent = new Date().getFullYear();

  if (P.cv) { $("cv").href = P.cv; $("cv").hidden = false; }
  if (P.foto) {
    $("foto").src = P.foto; $("foto").alt = "Foto de " + P.nombre;
    $("foto").hidden = false; $("ilustracion").style.display = "none";
  }

  $("stack").innerHTML = P.stack.map((s) => `<li>${tile(s)}</li>`).join("");
  $("cifras").innerHTML = P.cifras.map((c) =>
    `<li><div class="stats__ico">${icon(c.icono)}</div><div><strong>${esc(c.valor)}</strong><span>${esc(c.texto)}</span></div></li>`).join("");
  $("exp").innerHTML = P.experiencia.map((e) =>
    `<li class="job"><p class="job__date">${esc(e.fechas)}</p><h3>${esc(e.cargo)}</h3><p class="job__co">${esc(e.empresa)}</p><ul class="job__list">${e.logros.map((l) => `<li>${esc(l)}</li>`).join("")}</ul><ul class="tags">${e.tags.map((t) => `<li>${esc(t)}</li>`).join("")}</ul></li>`).join("");
  $("formacion").innerHTML = P.formacion.map((f) =>
    `<li><strong>${esc(f.titulo)}</strong><span>${esc(f.lugar)}</span><span>${esc(f.fecha)}</span></li>`).join("");
  $("habs").innerHTML =P.habilidades.map((h) => {
    const [txt, pct] = NIVELES[h.nivel] || NIVELES.intermedio;
    return `<li class="skill">${tile(h.id)}<span class="skill__name">${esc(h.nombre)}</span><span class="skill__lvl">${txt}</span><div class="bar"><i style="width:${pct}%"></i></div></li>`;
  }).join("");

  const cards = $("cards");
  cards.innerHTML = P.proyectos.map((p, i) => {
    const link = p.enlace
      ? `<a class="card__link" href="${esc(p.enlace)}" target="_blank" rel="noopener">Ver proyecto ↗</a>`
      : `<span class="card__link card__link--off">Código privado</span>`;
    return `<article class="card"><span class="card__num">${String(i + 1).padStart(2, "0")}</span><div class="card__art">${art(p.visual)}</div><div class="card__body"><h3>${esc(p.titulo)}</h3><p>${esc(p.resumen)}</p><ul class="tags">${p.tags.map((t) => `<li>${esc(t)}</li>`).join("")}</ul>${link}</div></article>`;
  }).join("");

  const C = P.contacto;
  const items = [
    C.github && ["github", C.github, C.github.replace("https://github.com/", "github.com/")],
    C.linkedin && ["linkedin", C.linkedin, "LinkedIn"],
    C.email && ["email", "mailto:" + C.email, C.email],
    C.telefono && ["telefono", "tel:" + C.telefono.replace(/\s/g, ""), C.telefono],
  ].filter(Boolean);
  $("enlaces").innerHTML = items.map(([i, h, t]) =>
    `<li><a href="${esc(h)}"${h.startsWith("http") ? ' target="_blank" rel="noopener"' : ""}>${icon(i)}${esc(t)}</a></li>`).join("");
  $("cta").href = C.email ? "mailto:" + C.email : C.linkedin || C.github;
  if (C.email) document.querySelector(".nav__cta").href = "mailto:" + C.email;
  else { $("cta").target = "_blank"; $("cta").rel = "noopener"; }

  // Paginador del carrusel
  const pager = $("pager");
  const paginas = () => {
    const card = cards.firstElementChild;
    if (!card) return 1;
    const paso = card.offsetWidth + parseFloat(getComputedStyle(cards).columnGap);
    return Math.max(1, Math.ceil((cards.scrollWidth - cards.clientWidth - 8) / paso) + 1);
  };
  const paso = () => cards.firstElementChild.offsetWidth + parseFloat(getComputedStyle(cards).columnGap);
  const marcar = () => {
    const i = Math.round(cards.scrollLeft / paso());
    [...pager.children].forEach((b, n) => {
      b.classList.toggle("on", n === i);
      b.setAttribute("aria-current", n === i);
    });
  };
  const armar = () => {
    const n = paginas();
    pager.hidden = n < 2;
    pager.innerHTML = Array.from({ length: n }, (_, i) => `<button type="button" aria-label="Ir a la posición ${i + 1}"></button>`).join("");
    [...pager.children].forEach((b, i) => b.addEventListener("click", () => cards.scrollTo({ left: i * paso(), behavior: "smooth" })));
    marcar();
  };
  armar();
  cards.addEventListener("scroll", () => requestAnimationFrame(marcar), { passive: true });
  addEventListener("resize", armar);

  // Menú móvil
  const menu = $("menu"), toggle = $("toggle");
  const abrir = (v) => { menu.classList.toggle("open", v); toggle.setAttribute("aria-expanded", v); };
  toggle.addEventListener("click", () => abrir(!menu.classList.contains("open")));
  menu.addEventListener("click", (e) => { if (e.target.tagName === "A") abrir(false); });

  // Sección activa en la navegación
  const enlaces = [...menu.querySelectorAll("a")];
  const obs = new IntersectionObserver((es) => {
    es.forEach((e) => {
      if (e.isIntersecting) enlaces.forEach((a) => a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id));
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  document.querySelectorAll("main section[id]").forEach((s) => obs.observe(s));
})();
