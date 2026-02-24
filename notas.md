/* CIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLECIRCLE==CIRCLE */
/* Contenedor de la lista */
.projects-list {
    display: flex;
    flex-direction: column;
    gap: 40px;
}

/* La Card combinada */
.project-card {
    position: relative; /* Necesario para el círculo animado */
    overflow: hidden;   /* Corta el círculo cuando sale de la card */
    padding: 25px;      /* Un poco más de aire */
    border-radius: 15px;
    background: rgba(105, 13, 197, 0.103); /* El color base de Uiverse */
    transition: all 0.5s ease;
    border: 1px solid rgba(255, 255, 255, 0.05); /* Toque extra de cristal */
}

/* El círculo animado de fondo (Pseudo-elemento) */
.project-card::before {
    content: "";
    height: 100px;
    width: 100px;
    position: absolute;
    top: -40%;
    left: -20%;
    border-radius: 50%;
    border: 35px solid rgba(255, 255, 255, 0.102);
    transition: all .8s ease;
    filter: blur(.5rem);
    pointer-events: none; /* Para que no interfiera con los clics */
}

/* Hover de la card: cambia fondo y mueve el círculo */
.project-card:hover {
    background-color: rgba(30, 41, 59, 0.5); /* Tu color original de hover */
    transform: translateY(-5px); /* Efecto sutil de elevación */
}

.project-card:hover::before {
    width: 140px;
    height: 140px;
    top: -30%;
    left: 70%; /* Movido a la derecha para que recorra la card */
    filter: blur(0rem);
}

/* Títulos y Enlaces */
.project-title a {
    color: #e2e8f0;
    text-decoration: none;
    font-size: 1.3rem;
    font-weight: 900; /* Estilo bold de Uiverse */
    position: relative;
    z-index: 1;
}

/* Descripción */
.project-description {
    font-size: 0.95rem;
    margin: 15px 0;
    color: rgba(240, 248, 255, 0.8); /* Un poco más legible */
    position: relative;
    z-index: 1;
}

/* Tus etiquetas tecnológicas intactas */
.tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 0;
    list-style: none;
    position: relative;
    z-index: 1;
}

.tech-tags li {
    background: rgba(45, 212, 191, 0.15);
    color: #5eead4; 
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: bold;
}

<!-- ================================================================================================================================================ -->