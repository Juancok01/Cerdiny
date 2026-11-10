/* Todo el contenido de la página vive aquí. Edita este archivo y recarga. */
window.PERFIL = {
  nombre: "Juan Cruz",
  nombreCorto: "Juan",

  // Pon aquí tu foto, por ejemplo "img/foto.png". Vacío = ilustración de datos.
  foto: "img/foto.png",
  // Coloca tu PDF en la carpeta y pon la ruta, por ejemplo "cv.pdf". Vacío = se oculta el botón.
  cv: "Juan-David-Cruz-Cardenas-CV.pdf",

  contacto: {
    github: "https://github.com/Juancok01",
    linkedin: "https://www.linkedin.com/in/juan-cruz-datos/",
    email: "juan.cruzcardenas011@gmail.com",
    telefono: "", // Vacío = no se muestra
  },

  // Herramientas que aparecen debajo del título
  stack: ["sql", "postgres", "mysql", "python", "athena", "bigquery", "quicksight"],

  // Cifras tomadas del CV
  cifras: [
    { icono: "reloj", valor: "3.5 años", texto: "De experiencia en datos" },
    { icono: "migracion", valor: "65%", texto: "Menos tiempo de respuesta" },
    { icono: "tabla", valor: "40%", texto: "Menos errores de ingesta" },
    { icono: "proyecto", valor: "4", texto: "Proyectos de datos" },
  ],

  experiencia: [
    {
      cargo: "Analista de Datos",
      empresa: "Pasar Express",
      fechas: "May 2025 – Ago 2026",
      logros: [
        "65% menos tiempo de respuesta del sistema optimizando consultas SQL.",
        "Tableros en AWS QuickSight y R Shiny construidos con los stakeholders.",
        "Monitoreo centralizado de KPIs para decisiones sobre proveedores y entregas.",
      ],
      tags: ["PostgreSQL", "Python", "R", "AWS Athena", "QuickSight"],
    },
    {
      cargo: "Administrador de Bases de Datos",
      empresa: "Sinergia Red",
      fechas: "Ago 2024 – Dic 2025",
      logros: [
        "Flujos ETL con Python y pandas para procesar catálogos e inventarios de forma masiva.",
        "40% menos errores manuales de ingesta con scripts de limpieza.",
        "30% más velocidad de acceso a la información con mejoras estructurales en MySQL.",
      ],
      tags: ["SQL", "MySQL", "Python", "ETL"],
    },
    {
      cargo: "Auxiliar Analista de Datos y Procesos",
      empresa: "Logytech Mobile Colombia",
      fechas: "May 2023 – Jul 2024",
      logros: [
        "Validación de datos liderando a un equipo de 3 personas.",
        "15% menos discrepancias de auditoría con limpieza exhaustiva de datos.",
        "30% menos tiempo en reportes operativos automatizando hojas de cálculo.",
      ],
      tags: ["Excel", "Bases de datos"],
    },
  ],

  formacion: [
    { titulo: "Ingeniería de Sistemas", lugar: "Universidad INCCA de Colombia", fecha: "Grado esperado Ago 2027" },
    { titulo: "Tecnólogo en Gestión de Sistemas de la Información", lugar: "Fundación de Educación Superior San José", fecha: "Jun 2025" },
    { titulo: "Data Engineer Associate", lugar: "DataCamp", fecha: "Oct 2025" },
    { titulo: "SQL Associate", lugar: "DataCamp", fecha: "Mar 2025" },
    { titulo: "Microsoft Office Specialist: Excel", lugar: "Microsoft", fecha: "Mar 2025" },
  ],

  // nivel: "avanzado" | "intermedio" | "aprendiendo"
  habilidades: [
    { id: "sql", nombre: "SQL", nivel: "avanzado" },
    { id: "postgres", nombre: "PostgreSQL", nivel: "avanzado" },
    { id: "mysql", nombre: "MySQL", nivel: "avanzado" },
    { id: "python", nombre: "Python", nivel: "intermedio" },
    { id: "pandas", nombre: "pandas", nivel: "intermedio" },
    { id: "etl", nombre: "Pipelines ETL/ELT", nivel: "intermedio" },
    { id: "athena", nombre: "AWS Athena", nivel: "intermedio" },
    { id: "bigquery", nombre: "BigQuery", nivel: "intermedio" },
    { id: "quicksight", nombre: "Amazon QuickSight", nivel: "intermedio" },
    { id: "looker", nombre: "Looker Studio", nivel: "intermedio" },
    { id: "shiny", nombre: "R Shiny", nivel: "intermedio" },
    { id: "excel", nombre: "Microsoft Excel", nivel: "avanzado" },
  ],

  /* Para subir un proyecto nuevo, copia un bloque y cambia los textos.
     visual: "pipeline" | "embudo" | "ventas" | "excel" | "er" | "seguridad" | "migraciones"
     enlace: URL del repositorio o demo. Vacío = muestra "Código privado". */
  proyectos: [
    {
      titulo: "Pipeline de cierre de caja",
      resumen: "Lee los turnos cerrados en Postgres, calcula esperado contra contado y avisa al dueño por correo sin repetir envíos.",
      tags: ["Python", "pandas", "PostgreSQL", "GitHub Actions"],
      visual: "pipeline",
      enlace: "https://github.com/Juancok01/arqueo_cierre_pipeline",
    },
    {
      titulo: "Analítica de un menú digital",
      resumen: "Eventos personalizados en GA4 con Google Tag Manager, embudo con campos calculados y un tablero que mide visitas, puntos de fuga y conversión a WhatsApp.",
      tags: ["GA4", "Tag Manager", "SQL", "Looker Studio"],
      visual: "embudo",
      enlace: "https://datastudio.google.com/reporting/f4f63d05-5762-4180-b082-8f0ad11e5da2/page/nkxpF",
    },
    {
      titulo: "Gestión de ventas en MySQL",
      resumen: "Base normalizada de 4 tablas con más de 15 consultas analíticas para reportes de clasificación ABC, márgenes y tendencias.",
      tags: ["MySQL", "SQL", "Modelo ER", "Reporting"],
      visual: "ventas",
      enlace: "https://github.com/Juancok01/ventas-database-mysql",
    },
    {
      titulo: "Deserción de empleados en un hospital",
      resumen: "Dashboard interactivo en Excel para identificar patrones de deserción, con filtros dinámicos y un buscador de empleados por identificación.",
      tags: ["Excel", "Tablas dinámicas", "Fórmulas", "Dashboard"],
      visual: "excel",
      enlace: "https://github.com/Juancok01/Dashboard-Desercion-Empleados-Hospital",
    },
  ],
};
