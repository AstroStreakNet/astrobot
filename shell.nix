
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python311.withPackages (ps: [
      ps.discordpy
      ps.python-dotenv
      ps.aiocron
    ]))
  ];
}

