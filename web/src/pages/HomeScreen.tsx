import React from 'react';

export const HomeScreen: React.FC = () => {
  return (
    <div className="bg-[#f9f9ff] text-[#0e1c2f] antialiased min-h-screen flex flex-col font-sans">
      {/* TOP APP BAR */}
      <header className="sticky top-0 z-50 bg-[#f9f9ff] border-b border-[#c1c6d5] shadow-sm transition-colors duration-150">
        <div className="flex justify-between items-center w-full px-4 h-14 max-w-7xl mx-auto">
          {/* Logo & Identity */}
          <div className="flex items-center gap-3">
            <div className="flex items-center justify-center w-8 h-8 rounded bg-[#004e9f] text-white">
              <span className="material-symbols-outlined text-lg">admin_panel_settings</span>
            </div>
            <div>
              <a className="text-xl font-bold text-[#004e9f] tracking-tight leading-none block" href="#">
                MedChain OS
              </a>
              <span className="text-[10px] font-bold text-[#414753] block tracking-wider uppercase opacity-85">
                Decentralized Healthcare Infrastructure
              </span>
            </div>
          </div>

          {/* Navigation Links (Web Desktop) */}
          <nav className="hidden lg:flex items-center gap-6 text-sm font-semibold text-[#414753]">
            <a className="hover:text-[#004e9f] transition-colors" href="#solutions">Solutions</a>
            <a className="hover:text-[#004e9f] transition-colors" href="#triage">Triage Clinique</a>
            <a className="hover:text-[#004e9f] transition-colors" href="#fefo">Pharmacie FEFO</a>
            <a className="hover:text-[#004e9f] transition-colors" href="#blood">Banque de Sang</a>
            <a className="hover:text-[#004e9f] transition-colors" href="#ledger">Grand Livre &amp; Sécurité</a>
            <a className="hover:text-[#004e9f] transition-colors" href="#architecture">Architecture</a>
          </nav>

          {/* Status Badge & Actions */}
          <div className="flex items-center gap-3">
            <div className="hidden sm:flex items-center gap-2 px-2.5 py-1 bg-[#f0f3ff] rounded border border-[#c1c6d5]">
              <span className="w-2 h-2 rounded-full bg-[#006b58] animate-pulse"></span>
              <span className="font-mono text-xs text-[#006b58] font-semibold">Mainnet Live · 99.99% · ISO 20022</span>
            </div>
            <a className="hidden md:inline-flex items-center gap-1.5 px-3 py-1.5 rounded text-sm font-semibold border border-[#004e9f] text-[#004e9f] hover:bg-[#e7eeff] transition-colors" href="#docs">
              <span className="material-symbols-outlined text-base">description</span>
              <span>Documentation</span>
            </a>
            <a className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded bg-[#0066cc] text-white hover:bg-[#004e9f] transition-all shadow-sm active:scale-95 text-sm font-semibold" href="#portals">
              <span className="material-symbols-outlined text-base">lock_clock</span>
              <span className="hidden sm:inline">Portail Sécurisé</span>
              <span className="sm:hidden">Connexion</span>
            </a>
          </div>
        </div>
      </header>

      {/* SUBHEADER TICKER */}
      <div className="bg-[#243145] text-[#ebf1ff] py-1.5 px-4 text-xs font-mono border-b border-gray-700">
        <div className="max-w-7xl mx-auto flex items-center justify-between overflow-x-auto whitespace-nowrap gap-6">
          <div className="flex items-center gap-4">
            <span className="flex items-center gap-1.5 text-[#5ffbd6]">
              <span className="material-symbols-outlined text-sm">verified_user</span>
              SHA-256 Node: #4092-B7
            </span>
            <span className="opacity-50">|</span>
            <span>TPS Peak: <strong className="text-white">128.4 tx/s</strong></span>
            <span className="opacity-50">|</span>
            <span>Redis Mutex Collisions: <strong className="text-[#5ffbd6]">0 (0.00%)</strong></span>
            <span className="opacity-50">|</span>
            <span>Preuves Merkle: <strong className="text-[#5ffbd6]">100% Intègres</strong></span>
          </div>
          <div className="flex items-center gap-3 opacity-75">
            <span className="w-1.5 h-1.5 rounded-full bg-[#5ffbd6]"></span>
            <span>48 Hôpitaux Provinciaux Synchronisés</span>
            <span className="hidden md:inline opacity-40">· Latence Edge: 42ms</span>
          </div>
        </div>
      </div>

      {/* HERO SECTION */}
      <section className="relative min-h-[580px] lg:min-h-[660px] flex items-center overflow-hidden border-b border-[#c1c6d5]">
        <div className="absolute inset-0 z-0">
          <img 
            alt="Telemetry center in high-tech hospital" 
            className="w-full h-full object-cover filter saturate-90 contrast-105" 
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuA7VxxwPCo79mafmAwDC32blCDqtu6wXLDRj7FK8bo8-tvpRll--nzrX5SZIdBP3QNFMq1994YFF_rANp5P0NYRtenqFf0zSq9Ah-fuDPYjLYjUrzCobfzfY81lq3jYSIthKv7L1-NZktN_5qe8z0qcBti3LfwDtBi9lAszCCQcnAWGSoimtroKeqWKBVimqXAGO4x2_1qCrDkjrjUss-vPLu2-VZ0Z9UeXHzA68j8"
          />
          <div className="absolute inset-0 bg-gradient-to-r from-[#0B192C]/95 via-[#0B192C]/85 to-[#004e9f]/70 mix-blend-multiply"></div>
          <div className="absolute inset-0 bg-gradient-to-t from-[#0B192C] via-transparent to-[#0B192C]/40"></div>
          <div className="absolute inset-0 backdrop-blur-[1.5px] bg-[#0e1c2f]/20"></div>
        </div>

        <div className="relative z-10 max-w-7xl mx-auto px-4 py-16 lg:py-24 w-full">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div className="lg:col-span-8 space-y-6">
              <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/20 text-white">
                <span className="material-symbols-outlined text-[#5ffbd6] text-base">health_and_safety</span>
                <span className="text-xs font-bold tracking-wide uppercase">
                  Système d'Exploitation Clinique Sécurisé &amp; Décentralisé
                </span>
              </div>
              <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-white tracking-tight leading-tight max-w-3xl">
                L'Infrastructure de Confiance pour la Santé Connectée et les Marchés Émergents
              </h1>
              <p className="text-lg text-white/85 max-w-2xl leading-relaxed">
                Triage clinique d'urgence, traçabilité pharmaceutique FEFO inviolable, coordination instantanée des réserves sanguines et passerelles financières Mobile Money validées sous preuve cryptographique SHA-256.
              </p>
              <div className="flex flex-wrap items-center gap-4 pt-2">
                <a className="inline-flex items-center gap-2.5 px-6 py-3.5 rounded bg-[#0066cc] text-white font-semibold shadow-md hover:bg-[#004e9f] transition-all active:scale-95" href="#portals">
                  <span className="material-symbols-outlined text-xl">stethoscope</span>
                  <span>Accéder aux Portails Cliniques</span>
                </a>
                <a className="inline-flex items-center gap-2 px-5 py-3.5 rounded bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/30 text-white font-semibold transition-all" href="#architecture">
                  <span className="material-symbols-outlined text-xl">terminal</span>
                  <span>Explorer l'Architecture &amp; Démo</span>
                </a>
              </div>
              <div className="pt-4 flex flex-wrap items-center gap-6 text-xs text-white/70 font-mono">
                <span className="flex items-center gap-1.5">
                  <span className="material-symbols-outlined text-[#5ffbd6] text-base">lock</span> Chiffrement RSA-4096
                </span>
                <span className="flex items-center gap-1.5">
                  <span className="material-symbols-outlined text-[#5ffbd6] text-base">sync_saved_locally</span> Zero Data-Loss Cache Offline
                </span>
                <span className="flex items-center gap-1.5">
                  <span className="material-symbols-outlined text-[#5ffbd6] text-base">payments</span> Interopérabilité Orange &amp; MTN MoMo
                </span>
              </div>
            </div>

            {/* Right Telemetry Widget */}
            <div className="lg:col-span-4">
              <div className="bg-white/95 backdrop-blur-md rounded-lg border border-[#D2DEEC] p-5 text-[#0e1c2f] shadow-xl space-y-4">
                <div className="flex items-center justify-between border-b border-[#c1c6d5] pb-3">
                  <div className="flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full bg-[#006b58]"></span>
                    <span className="text-xs font-bold text-[#004e9f]">NOEUD DE SANTÉ RÉGIONAL</span>
                  </div>
                  <span className="font-mono text-xs px-2 py-0.5 rounded bg-[#e7eeff] text-[#414753]">#HUB-CENTRAL</span>
                </div>
                <div className="space-y-3 font-mono text-xs">
                  <div className="flex justify-between items-center bg-[#f0f3ff] p-2 rounded border border-[#c1c6d5]/60">
                    <span className="text-[#414753]">Intégrité Blockchain</span>
                    <span className="text-[#006b58] font-semibold flex items-center gap-1">
                      <span className="material-symbols-outlined text-sm">check_circle</span> 100.0% Validée
                    </span>
                  </div>
                  <div className="flex justify-between items-center bg-[#f0f3ff] p-2 rounded border border-[#c1c6d5]/60">
                    <span className="text-[#414753]">Temps Moyen Triage P1</span>
                    <span className="text-[#004e9f] font-bold">1 min 42 sec</span>
                  </div>
                  <div className="flex justify-between items-center bg-[#f0f3ff] p-2 rounded border border-[#c1c6d5]/60">
                    <span className="text-[#414753]">Poches O- Sang Urgence</span>
                    <span className="text-[#ba1a1a] font-bold flex items-center gap-1">
                      <span className="w-2 h-2 rounded-full bg-[#ba1a1a] animate-ping"></span> 14 Unités Disponibles
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* PORTALS SECTION (5 Personas RBAC) */}
      <section className="py-16 bg-[#f0f3ff] border-b border-[#c1c6d5]" id="portals">
        <div className="max-w-7xl mx-auto px-4 space-y-10">
          <div className="max-w-3xl space-y-2">
            <div className="text-xs font-bold text-[#004e9f] tracking-wider uppercase flex items-center gap-1.5">
              <span className="material-symbols-outlined text-base">shield</span> Architecture Multi-Rôles RBAC Sécurisée
            </div>
            <h2 className="text-2xl sm:text-3xl font-bold text-[#0e1c2f] tracking-tight">
              Portails d'Accès Dédiés &amp; Écosystème Décentralisé
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* 1. Patient Portal */}
            <div className="bg-white rounded-lg border border-[#D2DEEC] p-6 shadow-sm hover:border-[#004e9f] transition-all flex flex-col justify-between group">
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="w-12 h-12 rounded bg-[#e7eeff] flex items-center justify-center text-[#004e9f] group-hover:bg-[#004e9f] group-hover:text-white transition-colors">
                    <span className="material-symbols-outlined text-2xl">personal_injury</span>
                  </div>
                  <span className="font-mono text-xs px-2 py-0.5 rounded bg-[#e7eeff] text-[#414753]">PORTAIL 01</span>
                </div>
                <h3 className="text-lg font-semibold text-[#0e1c2f]">Portail Patient &amp; Identité Biométrique</h3>
                <p className="text-sm text-[#414753]">
                  Carnet de santé inviolable, ordonnances dématérialisées avec code QR certifié, réservation avec verrou 5 min et règlement Mobile Money (Orange / MTN).
                </p>
              </div>
              <div className="pt-6">
                <a className="w-full py-2.5 px-4 rounded bg-[#e7eeff] hover:bg-[#d6e3fe] text-[#004e9f] font-semibold text-sm flex items-center justify-between border border-[#c1c6d5] transition-colors" href="#">
                  <span>Accéder à l'Espace Patient</span>
                  <span className="material-symbols-outlined text-base">arrow_forward</span>
                </a>
              </div>
            </div>

            {/* 2. Doctor Portal */}
            <div className="bg-white rounded-lg border border-[#D2DEEC] p-6 shadow-sm hover:border-[#004e9f] transition-all flex flex-col justify-between group">
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="w-12 h-12 rounded bg-[#e7eeff] flex items-center justify-center text-[#004e9f] group-hover:bg-[#004e9f] group-hover:text-white transition-colors">
                    <span className="material-symbols-outlined text-2xl">stethoscope</span>
                  </div>
                  <span className="font-mono text-xs px-2 py-0.5 rounded bg-[#e7eeff] text-[#414753]">PORTAIL 02</span>
                </div>
                <h3 className="text-lg font-semibold text-[#0e1c2f]">Doctor Triage &amp; Urgence Vitale</h3>
                <p className="text-sm text-[#414753]">
                  Triage P1-P3, téléconsultation chiffrée WebRTC et signature d'ordonnances RSA-4096.
                </p>
              </div>
              <div className="pt-6">
                <a className="w-full py-2.5 px-4 rounded bg-[#e7eeff] hover:bg-[#d6e3fe] text-[#004e9f] font-semibold text-sm flex items-center justify-between border border-[#c1c6d5] transition-colors" href="#">
                  <span>Ouvrir la Console Clinique</span>
                  <span className="material-symbols-outlined text-base">arrow_forward</span>
                </a>
              </div>
            </div>

            {/* 3. Pharmacy FEFO Portal */}
            <div className="bg-white rounded-lg border border-[#D2DEEC] p-6 shadow-sm hover:border-[#004e9f] transition-all flex flex-col justify-between group">
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="w-12 h-12 rounded bg-[#e7eeff] flex items-center justify-center text-[#004e9f] group-hover:bg-[#004e9f] group-hover:text-white transition-colors">
                    <span className="material-symbols-outlined text-2xl">medication</span>
                  </div>
                  <span className="font-mono text-xs px-2 py-0.5 rounded bg-[#e7eeff] text-[#414753]">PORTAIL 03</span>
                </div>
                <h3 className="text-lg font-semibold text-[#0e1c2f]">Pharmacie &amp; Traçabilité FEFO</h3>
                <p className="text-sm text-[#414753]">
                  Gestion First-Expired First-Out, scanner d'ordonnances QR et prévention des contrefaçons.
                </p>
              </div>
              <div className="pt-6">
                <a className="w-full py-2.5 px-4 rounded bg-[#e7eeff] hover:bg-[#d6e3fe] text-[#004e9f] font-semibold text-sm flex items-center justify-between border border-[#c1c6d5] transition-colors" href="#">
                  <span>Gérer l'Officine FEFO</span>
                  <span className="material-symbols-outlined text-base">arrow_forward</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomeScreen;