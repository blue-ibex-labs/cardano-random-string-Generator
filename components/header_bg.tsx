
// import { Suspense } from "react"
// import { Canvas, useLoader } from "@react-three/fiber"
// import { Environment, OrbitControls } from "@react-three/drei"
// import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader"

// const Model = () => {
<<<<<<< HEAD
//     const gltf = useLoader(GLTFLoader, "/mount/scene.gltf");
//     return (
//         <>
//             <primitive object={gltf.scene} scale={0.001} />
//         </>
//     );
// };
// import Parallax from 'react-rellax'
=======
//     const gltf = useLoader(GLTFLoader, "/scene.gltf");
//     return (
//         <>
//             <primitive object={gltf.scene} scale={0.4} />
//         </>
//     );
// };
>>>>>>> parent of 0a987173 (removed some junk)

export default function HeaderBG() {
    return (
        <div >


            <div className="globe">
<<<<<<< HEAD
                {/* <Canvas shadows dpr={[1, 2]} camera={{ position: [1, 4, 9], fov: 8 }}>
=======
                {/* <Canvas shadows dpr={[1, 2]} camera={{ position: [9, 4, 1], fov: 20 }}>
>>>>>>> parent of 0a987173 (removed some junk)
                    <Suspense fallback={null}>
                        <Model />
                        <Environment preset="dawn" />

                    </Suspense>
<<<<<<< HEAD
                    <OrbitControls autoRotate={true} autoRotateSpeed={2} enableRotate={false} enableZoom={false} />
=======
                    <OrbitControls autoRotate={true} enableRotate={false} autoRotateSpeed={2} enableZoom={false} />
>>>>>>> parent of 0a987173 (removed some junk)
                </Canvas> */}
                <div className="para">
                    <div className="mx-auto max-w-3xl text-center">
                        <h1 className=" text-3xl font-extrabold text-blue-600 sm:text-8xl">BLUE IBEX DAO.</h1>

                        <p className="mx-auto mt-4 max-w-xl sm:text-4xl sm:leading-relaxed">
                            DEFi For Everyone!
                        </p>

                        <div className="mt-8 flex flex-wrap justify-center gap-4">
                            {/* <Parallax speed={1}>
                                <a
                                    className="block w-full rounded border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-blue-600 focus:outline-none focus:ring active:text-opacity-75 sm:w-auto"
                                    href="#start"
                                >
                                    Get Started
                                </a>
                            </Parallax> */}
                            <a
                                className="block w-full rounded border border-blue-600 bg-blue-600 px-12 py-3 text-sm font-medium text-white hover:bg-transparent hover:text-blue-600 focus:outline-none focus:ring active:text-opacity-75 sm:w-auto"
                                href="#start"
                            >
                                Get Started
                            </a>

                            <a
                                className="block w-full rounded border border-blue-600 px-12 py-3 text-sm font-medium text-blue-600 hover:bg-blue-600 hover:text-white focus:outline-none focus:ring active:bg-blue-500 sm:w-auto"
                                href="/about"
                            >
                                Learn More
                            </a>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    )
}
