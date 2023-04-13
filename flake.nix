{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in {
        packages.default =
          pkgs.poetry2nix.mkPoetryApplication { projectDir = self; };

        devShells.default = pkgs.mkShellNoCC {
          packages = with pkgs; [
            (poetry2nix.mkPoetryEnv { projectDir = self; })
            poetry
          ];
        };
      });
}
