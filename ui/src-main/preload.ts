import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('api', {
  getContext: async () => ipcRenderer.invoke('getContext'),
  setContext: async (newContext) =>
    ipcRenderer.invoke('setContext', newContext),
});
