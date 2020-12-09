import Menu from "./Menu/Menu";

const Header = (props) => {
  return (
    <header className="container">
      <h1 className="text-center bg-success bg-gradient p-3 text-white text-uppercase fs-2 my-2">
        IBMWP
      </h1>
      <Menu />
    </header>
  );
};

export default Header;
