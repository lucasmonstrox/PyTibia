const { override } = require('customize-cra');

// Add this function to override() only when "nodeIntegration" is true,
// otherwise Electron will report "require is not defiend" error.
// tslint-disable-next-line
function addRendererTarget(config) {
  config.target = 'electron-renderer';
  return config;
}

module.exports = override();
