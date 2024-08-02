interface ISiteMetadataResult {
  siteTitle: string;
  siteUrl: string;
  description: string;
  keywords: string;
  logo: string;
  navLinks: {
    name: string;
    url: string;
  }[];
}

const data: ISiteMetadataResult = {
  siteTitle: 'Riding Map',
  siteUrl: '',
  logo: 'https://avatars.githubusercontent.com/u/26806882?v=4',
  description: '神骏的骑行数据',
  keywords: 'workouts, running, cycling, riding, roadtrip, hiking, swimming',
  navLinks: [
    {
      name: 'GitHub',
      url: 'https://github.com/conanyangqun',
    },
    {
      name: 'About',
      url: 'https://github.com/conanyangqun/riding-page/blob/master/README-CN.md',
    },
    {
      name: 'vercel站点',
      url: 'https://riding-page-eight.vercel.app/',
    },
    {
      name: 'cloudflare站点',
      url: 'https://riding-page.pages.dev/',
    }
  ],
};

export default data;
