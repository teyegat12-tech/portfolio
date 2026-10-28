import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const groups=JSON.parse(await fs.readFile(path.join(root,'projects.json'),'utf8'));
const ids=new Set();let count=0;
for(const group of groups){
  for(const key of ['id','kicker','title','description'])if(typeof group[key]!=='string')throw Error(`Missing section ${key}`);
  for(const project of group.projects){
    for(const key of ['id','status','title','description','action'])if(typeof project[key]!=='string'||!project[key].trim())throw Error(`Missing project ${key}`);
    if(ids.has(project.id))throw Error(`Duplicate project ${project.id}`);ids.add(project.id);count++;
    for(const link of project.links){
      if(!link.label||Boolean(link.url)===Boolean(link.local))throw Error(`Invalid link in ${project.id}`);
      if(link.url&&!/^https?:\/\//.test(link.url))throw Error(`Invalid URL in ${project.id}`);
      if(link.local&&link.local.startsWith('/'))throw Error(`Absolute private path in ${project.id}`);
    }
  }
}
for(const file of ['index.html','style.css','app.js']){
  const source=await fs.readFile(path.join(root,file),'utf8');
  if(/figma\.com\/api\/mcp\/asset|file:\/\//.test(source))throw Error(`Temporary or file URL in ${file}`);
  for(const match of source.matchAll(/assets\/[\w./-]+\.(?:svg|webp|png|ttf)/g)){
    const stat=await fs.stat(path.join(root,match[0]));if(!stat.size)throw Error(`Empty asset ${match[0]}`);
  }
}
console.log(`OK: ${groups.length} sections, ${count} projects; assets and links validated.`);
