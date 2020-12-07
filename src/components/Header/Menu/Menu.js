import { Link } from "react-router-dom";

const Menu = (props) => {
  return (
    <nav className="container">
      <ul className="row row-cols-auto g-2">
        <Link to="/" className="col">
          <li className="p-3 border bg-light">Inicio</li>
        </Link>
        <Link to="/key" className="col">
          <li className="p-3 border bg-light">Clave dicotómica</li>
        </Link>
        <Link to="/form" className="col">
          <li className="p-3 border bg-light">Formulario</li>
        </Link>
      </ul>
    </nav>
  );
};

export default Menu;
