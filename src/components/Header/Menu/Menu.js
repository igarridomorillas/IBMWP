import { Link } from "react-router-dom";

const Menu = (props) => {
  return (
    <nav className="container">
      <ul className="row align-items-start">
        <Link to="/" className="col-2">
          <li>Home</li>
        </Link>
        <Link to="/key" className="col-2">
          <li>Clave dicotómica</li>
        </Link>
        <Link to="/form" className="col-2">
          <li>Formulario</li>
        </Link>
      </ul>
    </nav>
  );
};

export default Menu;
